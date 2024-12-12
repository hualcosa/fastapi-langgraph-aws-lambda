import json
import logging
from fastapi import FastAPI
from mangum import Mangum
from typing import Dict, Any
from custom_lambda_utils.mhaite_langgraph import MhaiteCetep

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = FastAPI(root_path="/prod")
agent = MhaiteCetep()


@app.get("/")
async def root() -> dict:
    """Health check endpoint"""
    return {"status": "healthy"}


@app.post("/chat")
async def chat(request: Dict[str, Any]) -> dict:
    """
    Chat endpoint implementing the LangGraph conversation logic.

    Args:
        request (Dict[str, Any]): Request containing message and session_id
    Returns:
        dict: Response from the agent
    """
    pass  # Implement the LangGraph conversation logic here


def lambda_handler(event, context):
    logger.info(json.dumps(event))
    asgi_handler = Mangum(app)
    response = asgi_handler(event, context)
    logger.info(json.dumps(response))
    return response
