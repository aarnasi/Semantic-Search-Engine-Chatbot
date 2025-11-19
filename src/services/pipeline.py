"""Document ingestion pipeline orchestration."""

from __future__ import annotations

import logging
from typing import Optional

from langchain_core.documents import Document

from src.config import AppSettings
from src.embeddings import vector_store
from src.ingestion import pdf_loader
from src.processing import chunk_documents

logger = logging.getLogger(__name__)


class DocumentIngestionPipeline:
    """Coordinates PDF ingestion, chunking, and vector storage."""

    def __init__(self, settings: Optional[AppSettings] = None) -> None:
        self._settings = settings or AppSettings()

    def run(self, pdf_path: str) -> None:
        """Execute the ingestion pipeline."""

        documents = self._load_documents(pdf_path)
        if not documents:
            logger.error("No documents loaded from %s", pdf_path)
            return

        chunks = chunk_documents(documents, self._settings.chunking)
        if not chunks:
            logger.error("Chunking returned no documents.")
            return

        vector_store.generate_and_store_embeddings(
            chunks,
            self._settings.vector_store,
            self._settings.llm,
        )
        logger.info("Completed ingestion for %s", pdf_path)

    def _load_documents(self, pdf_path: str) -> Optional[list[Document]]:
        """Load documents using the ingestion module."""

        documents = pdf_loader.load_pdf(pdf_path)
        if documents is None:
            return None
        return list(documents)


