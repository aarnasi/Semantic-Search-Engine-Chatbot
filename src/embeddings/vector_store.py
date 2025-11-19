"""Vector store management."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS

from src.config import LLMConfig, VectorStoreConfig
from src.embeddings.embedder import get_embedder


def generate_and_store_embeddings(
    chunked_documents: Iterable[Document],
    vector_config: VectorStoreConfig,
    llm_config: LLMConfig,
) -> None:
    """Create embeddings for documents and persist them to FAISS."""

    vector_store = FAISS.from_documents(
        documents=list(chunked_documents),
        embedding=get_embedder(llm_config),
    )
    vector_store.save_local(str(vector_config.storage_path))


def load_vectorstore(
    vector_config: VectorStoreConfig,
    llm_config: LLMConfig,
) -> FAISS:
    """Load a persisted FAISS vector store."""

    path = Path(vector_config.storage_path)
    if not path.exists():
        raise FileNotFoundError(f"Vector store not found at {path}")
    return FAISS.load_local(
        str(path),
        get_embedder(llm_config),
        allow_dangerous_deserialization=True,
    )


