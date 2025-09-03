import os

import requests
from dotenv import load_dotenv


def load_dotenv_files() -> None:
    """Load environment variables from .env* files."""
    _env_files = [
        ".env",  # Global
        ".env.langflow.local",
    ]

    for env_file in _env_files:
        print(f"Loading {env_file}...")  # TODO use logger
        load_dotenv(env_file, override=True, verbose=True)


load_dotenv_files()

# TODO use pydantic-settings
# API Configuration
try:
    host = os.environ.get("LANGFLOW_SERVER_ADDRESS", "http://localhost:7861")
    api_key = os.environ["LANGFLOW_API_KEY"]
    flow_id = os.environ.get("LANGFLOW_FLOW_ID")
except KeyError:
    raise ValueError("Missing LANGFLOW_* variables. Please set your API key in the environment variables.")

url = f"{host}/api/v1/run/{flow_id}"  # The complete API endpoint URL for this flow

# Request payload configuration
payload = {"output_type": "chat", "input_type": "chat", "input_value": "hello world!"}

# Request headers
headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key,  # Authentication key from environment variable
}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")
