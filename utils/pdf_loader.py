from langchain_community.document_loaders import PyPDFLoader
import logging
from typing import Optional, List
from langchain_core.documents import Document

# Configure logging to display errors with a timestamp and log level
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to load a PDF file and return a list of Document objects
def load_pdf(path: str) -> Optional[List[Document]]:
    try:
        # Attempt to load and return the documents from the specified PDF path
        return PyPDFLoader(path).load()
    except ValueError as error:
        # Handle known value-related errors (e.g., invalid file path or format)
        logging.error(f"ValueError while loading PDF: {error}")
        return None
    except Exception as e:
        # Handle any other unexpected exceptions
        logging.error(f"Unexpected error while loading PDF: {e}")
        return None