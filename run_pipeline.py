"""CLI entry point for the ingestion pipeline."""

from __future__ import annotations

import logging
import sys

from src.core import configure_logging
from src.services import DocumentIngestionPipeline


def main(pdf_path: str) -> None:
    """Execute the enterprise pipeline to ingest documents."""

    configure_logging(logging.INFO)
    pipeline = DocumentIngestionPipeline()
    pipeline.run(pdf_path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run_pipeline.py <path_to_pdf>")
        sys.exit(1)

    main(sys.argv[1])


