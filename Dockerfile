# Use the latest version of the base Langflow image
FROM langflowai/langflow:latest

WORKDIR /app

# Copy flows, langflow-config-dir, and docker.env to the container
COPY containers/langflow/app/ /app
COPY docker.env /app/.env

# Optional: Copy custom components to the container
COPY src/hello_langflow/components /app/components

# Optional: Use custom dependencies
COPY pyproject.toml uv.lock /app/

# Command to run the Langflow server on port 7860
EXPOSE 7860
CMD ["langflow", "run", "--backend-only", "--env-file","/app/.env","--host", "0.0.0.0", "--port", "7860"]
