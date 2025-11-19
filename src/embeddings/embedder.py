"""Factory for embedding models."""

from __future__ import annotations

import logging
from functools import lru_cache

from langchain_core.embeddings import Embeddings
from langchain_ollama import OllamaEmbeddings

from src.config import LLMConfig

logger = logging.getLogger(__name__)


@lru_cache(maxsize=1)
def get_embedder(config: LLMConfig) -> Embeddings:
    """Return a cached instance of the Ollama embedding model."""

    try:
        return OllamaEmbeddings(model=config.model_name)
    except Exception as error:  # pylint: disable=broad-except
        logger.exception("Failed to initialize OllamaEmbeddings: %s", error)
        raise


