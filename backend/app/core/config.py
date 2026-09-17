"""
Application configuration settings.

Centralizes all configurable values (paths, model names, chunking params)
so they can be adjusted in one place.
"""

import os
from pathlib import Path


# ── Paths ──────────────────────────────────────────────────────────────
# Resolve paths relative to the *project root* (two levels above this file)
_BASE_DIR = Path(__file__).resolve().parent.parent.parent  # → backend/

DATA_FOLDER: str = os.getenv(
    "DATA_FOLDER",
    str(_BASE_DIR.parent / "data"),        # → rag-assistant-project/data
)

VECTOR_STORE_PATH: str = os.getenv(
    "VECTOR_STORE_PATH",
    str(_BASE_DIR / "data" / "vector_store"),  # → backend/data/vector_store
)


# ── Embedding model ───────────────────────────────────────────────────
EMBEDDING_MODEL_NAME: str = os.getenv(
    "EMBEDDING_MODEL_NAME",
    "all-MiniLM-L6-v2",
)


# ── ChromaDB ──────────────────────────────────────────────────────────
CHROMA_COLLECTION_NAME: str = os.getenv(
    "CHROMA_COLLECTION_NAME",
    "rag_collection",
)


# ── Ollama LLM ────────────────────────────────────────────────────────
OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "llama3")
OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")


# ── Chunking defaults ─────────────────────────────────────────────────
CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", "500"))
CHUNK_OVERLAP: int = int(os.getenv("CHUNK_OVERLAP", "50"))


# ── Retrieval ─────────────────────────────────────────────────────────
DEFAULT_TOP_K: int = int(os.getenv("DEFAULT_TOP_K", "3"))
