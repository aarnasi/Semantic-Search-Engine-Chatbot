import sys
import logging
from typing import Optional

from utils import pdf_loader
from utils import chunking
from embeddings import vector_store

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main(pdf_path: str) -> Optional[None]:
    """
    Orchestrates the PDF processing pipeline:
    - Loads a PDF file
    - Chunks its content
    - Generates and stores embeddings in a FAISS index
    """
    try:
        logging.info("Loading PDF...")
        text = pdf_loader.load_pdf(pdf_path)
        if not text:
            logging.error("Failed to load PDF or no content found.")
            return

        logging.info("Chunking text...")
        chunks = chunking.get_chunked_text(text)

        logging.info("Generating and storing embeddings in FAISS index...")
        vector_store.generate_and_store_embeddings_faiss(chunks)

        logging.info("Pipeline completed successfully.")

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}", exc_info=True)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        logging.error("Usage: python run_pipeline.py <path_to_pdf>")
        sys.exit(1)
    main(sys.argv[1])


