"""
Query route – POST /api/query

Accepts a user question, runs it through the RAG pipeline,
and returns the answer with source metadata.
"""

from fastapi import APIRouter, HTTPException

from backend.app.schemas.query import QueryRequest, QueryResponse
from backend.app.services.retrieval import retrieve_and_answer

router = APIRouter(prefix="/api", tags=["query"])


@router.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest) -> QueryResponse:
    """Answer a user question using Retrieval-Augmented Generation."""
    try:
        result = retrieve_and_answer(question=request.question)
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"RAG pipeline error: {exc}",
        ) from exc

    return QueryResponse(
        answer=result["answer"],
        sources=result["sources"],
    )
