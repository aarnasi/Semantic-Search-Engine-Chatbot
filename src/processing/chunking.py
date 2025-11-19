"""Responsible for turning documents into retrievable chunks."""

from __future__ import annotations

from typing import Iterable, List

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config import ChunkingConfig


def chunk_documents(
    documents: Iterable[Document],
    config: ChunkingConfig,
) -> List[Document]:
    """Split documents into overlapping chunks suitable for embedding."""

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.chunk_size,
        chunk_overlap=config.chunk_overlap,
        add_start_index=config.add_start_index,
    )
    return splitter.split_documents(list(documents))


