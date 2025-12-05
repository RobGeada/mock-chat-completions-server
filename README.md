# Mock Chat Completions Server

A simple FastAPI server that mocks the OpenAI `/v1/chat/completions` API endpoint. It logs incoming requests (headers and payload) and returns a dummy response.

## Features

- Receives POST requests at `/v1/chat/completions`
- Logs request headers and JSON payload (pretty-printed with timestamp)
- Returns a static, dummy chat-completion response
- Ready to run locally or in Podman/Docker

## Requirements

- Python 3.11+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)

## Running Locally

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Start the server:

    ```bash
    python server.py
    ```  
    The server will listen on `http://0.0.0.0:8081`.

## Running with Podman/Docker
### Using the pre-built container
1. Run the container
    ```hash
   podman run -p 8081:8081  quay.io/rgeada/mock-chat-completions-server:latest 
   ```
### Building the container yourself
1. Build the image:

    ```bash
    podman build -t mock-chat-completions .
    ```

2. Run the container:

    ```bash
    podman run -p 8081:8081 mock-chat-completions
    ```

