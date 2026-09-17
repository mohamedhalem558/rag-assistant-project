"""
Retrieval service – vector search + LLM answer generation.

Encapsulates the RAG pipeline:
  1. Encode the user query with SentenceTransformer.
  2. Search ChromaDB for the top-k most relevant chunks.
  3. Build a prompt from the retrieved context.
  4. Call Ollama (llama3) for the final answer.
"""

from __future__ import annotations

import logging
from typing import Any

import ollama
from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer

from backend.app.core.config import (
    CHROMA_COLLECTION_NAME,
    DEFAULT_TOP_K,
    EMBEDDING_MODEL_NAME,
    OLLAMA_MODEL,
    VECTOR_STORE_PATH,
)

logger = logging.getLogger(__name__)

# ── Lazy singletons ───────────────────────────────────────────────────
_embedding_model: SentenceTransformer | None = None
_chroma_collection: Any = None  # chromadb.Collection


def _get_embedding_model() -> SentenceTransformer:
    """Return the (cached) SentenceTransformer model."""
    global _embedding_model
    if _embedding_model is None:
        logger.info("Loading embedding model '%s' …", EMBEDDING_MODEL_NAME)
        _embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)
    return _embedding_model


def _get_chroma_collection():
    """Return the (cached) ChromaDB collection."""
    global _chroma_collection
    if _chroma_collection is None:
        logger.info("Connecting to ChromaDB at '%s' …", VECTOR_STORE_PATH)
        client = PersistentClient(path=VECTOR_STORE_PATH)
        _chroma_collection = client.get_or_create_collection(
            name=CHROMA_COLLECTION_NAME,
        )
    return _chroma_collection


# ── Public API ─────────────────────────────────────────────────────────

def retrieve_and_answer(question: str, top_k: int = DEFAULT_TOP_K) -> dict:
    """
    Run the full RAG pipeline for *question*.

    Returns a dict with:
        - ``answer``  : str   – the LLM-generated response.
        - ``sources`` : list  – simple string representations of sources.
    """
    # 1. Embed the query
    model = _get_embedding_model()
    query_embedding = model.encode([question]).tolist()

    # 2. Search ChromaDB
    collection = _get_chroma_collection()
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k,
    )

    retrieved_texts: list[str] = results["documents"][0] if results["documents"] else []
    retrieved_metas: list[dict] = results["metadatas"][0] if results["metadatas"] else []

    if not retrieved_texts:
        return {
            "answer": "I couldn't find any relevant information in the knowledge base.",
            "sources": [],
        }

    # 3. Build the prompt
    context = "\n\n".join(retrieved_texts)
    prompt = (
        "Use the following context to answer the question.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {question}"
    )

    # 4. Call Ollama
    logger.info("Calling Ollama model '%s' …", OLLAMA_MODEL)
    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )

    answer: str = response["message"]["content"]

    # 5. Package sources as simple strings to match the schema
    sources = [
        f"File: {meta.get('source', 'Unknown')}, Page: {meta.get('page', 'Unknown')}"
        for meta in retrieved_metas
    ]

    return {"answer": answer, "sources": sources}