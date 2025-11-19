"""Utilities for loading source documents."""

from __future__ import annotations

import logging
from typing import List, Optional

from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader

logger = logging.getLogger(__name__)


def load_pdf(path: str) -> Optional[List[Document]]:
    """Load a PDF from disk and return LangChain Document objects."""

    try:
        return PyPDFLoader(path).load()
    except ValueError as error:
        logger.error("Value error while loading PDF: %s", error)
        return None
    except Exception as error:  # pylint: disable=broad-except
        logger.exception("Unexpected error while loading PDF: %s", error)
        return None


