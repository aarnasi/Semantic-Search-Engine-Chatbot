"""Retrieval helpers for semantic search."""

from __future__ import annotations

from typing import List

from langchain_core.documents import Document

from src.config import AppSettings
from src.embeddings import vector_store


def get_context_chunks(query: str, settings: AppSettings) -> List[Document]:
    """Retrieve relevant context chunks for a query."""

    store = vector_store.load_vectorstore(
        settings.vector_store,
        settings.llm,
    )
    return store.similarity_search(query)


