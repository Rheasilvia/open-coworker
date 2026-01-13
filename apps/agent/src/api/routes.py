"""FastAPI routes for the agent service."""
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from src.agents.orchestrator import orchestrator

router = APIRouter()


class ChatRequest(BaseModel):
    """Request model for chat endpoint."""

    message: str


@router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "open-coworker-agent"}


@router.post("/chat")
async def chat(request: ChatRequest):
    """
    Chat endpoint with SSE streaming.

    Args:
        request: Chat request with message

    Returns:
        StreamingResponse with SSE format
    """

    async def generate():
        """Generate SSE stream."""
        try:
            async for chunk in orchestrator.process(request.message):
                # Send SSE formatted data
                yield f"data: {format_sse_data(chunk)}\n\n"
            # Send done signal
            yield "data: [DONE]\n\n"
        except Exception as e:
            error_data = format_sse_data(f"Error: {str(e)}")
            yield f"data: {error_data}\n\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


def format_sse_data(content: str) -> str:
    """Format content as SSE data."""
    import json

    return json.dumps({"content": content})
