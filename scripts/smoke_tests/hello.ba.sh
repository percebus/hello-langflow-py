#!/bin/bash

set -e

# Get API key from environment variable

if [ -z "$LANGFLOW_API_KEY" ]; then
  echo "Error: LANGFLOW_API_KEY environment variable not found. Please set your API key in the environment variables."
  exit 1
fi


set -x
url="${LANGFLOW_SERVER_ADDRESS}/api/v1/run/${LANGFLOW_FLOW_ID}"
set +x

# SRC: https://docs.langflow.org/get-started-quickstart
set -v
curl \
  --request POST \
  --url "${url}?stream=false" \
  --header "Content-Type: application/json" \
  --header "x-api-key: ${LANGFLOW_API_KEY}" \
  --data '{
      "output_type": "chat",
      "input_type": "chat",
      "input_value": "Hello"
    }'

set +v

set +e
