from typing import List

from langchain_core.documents import Document

from embeddings import vector_store

# Function to retrieve similar documents (context chunks) based on a query
def get_context_chunks(query) -> List[Document]:
    # Load the vector store and perform a similarity search using the input query
    # Returns a list of Document objects that are most similar to the query
    return vector_store.load_vectorstore().similarity_search(query)
