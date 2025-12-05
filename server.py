from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging
import uvicorn
import json
app = FastAPI()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("mock-chat-completions")

@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    payload = await request.json()

    log_msg = {}
    log_msg["headers"] = {k:v for k,v in request.headers.items()}
    log_msg["request"] = payload

    logger.info("Received Request:\n"+json.dumps(log_msg, indent=2))


    # Dummy response mimicking OpenAI's chat-completions format
    response = {
        "id": "chatcmpl-mock123",
        "object": "chat.completion",
        "created": 1234567890,
        "model": payload.get("model", "dummy-server"),
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": "This is a mock response."
                },
                "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 10,
            "completion_tokens": 5,
            "total_tokens": 15
        }
    }
    return JSONResponse(content=response)

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8081, reload=True)