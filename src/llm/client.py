"""LLM service responsible for answer generation."""

from __future__ import annotations

import logging
from typing import Optional

from langchain_ollama import ChatOllama

from src.config import AppSettings
from src.llm.prompt import BASE_PROMPT
from src.retrieval import retriever

logger = logging.getLogger(__name__)


class LLMService:
    """Encapsulates interactions with the chat model."""

    def __init__(self, settings: AppSettings) -> None:
        self._settings = settings
        self._model = ChatOllama(model=settings.llm.model_name)

    def generate_answer(self, query: str) -> Optional[str]:
        """Generate an answer for the supplied query."""

        context_documents = retriever.get_context_chunks(query, self._settings)
        context = "\n\n".join(doc.page_content for doc in context_documents)

        prompt = BASE_PROMPT.format(context=context, question=query)

        try:
            response = self._model.invoke(prompt)
            return getattr(response, "content", str(response))
        except Exception as error:  # pylint: disable=broad-except
            logger.exception("Failed to generate answer: %s", error)
            return None


