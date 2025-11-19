"""Centralized configuration objects for the application."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class ChunkingConfig:
    """Controls how documents are split into chunks."""

    chunk_size: int = 1000
    chunk_overlap: int = 200
    add_start_index: bool = True


@dataclass(frozen=True)
class VectorStoreConfig:
    """Settings for the FAISS vector store."""

    storage_path: Path = field(default_factory=lambda: Path("faiss_index"))


@dataclass(frozen=True)
class LLMConfig:
    """Settings for the LLM client."""

    model_name: str = "llama3"


@dataclass(frozen=True)
class AppSettings:
    """Aggregates all application settings."""

    chunking: ChunkingConfig = field(default_factory=ChunkingConfig)
    vector_store: VectorStoreConfig = field(default_factory=VectorStoreConfig)
    llm: LLMConfig = field(default_factory=LLMConfig)


