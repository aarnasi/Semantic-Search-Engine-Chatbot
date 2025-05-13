# Import the ChatOllama model from langchain_ollama for interacting with the LLaMA 3 language model
from langchain_ollama import ChatOllama

import retrieval.retierver as rt


# Function to initialize and return a chat model instance (LLaMA 3)
def get_chat_model():
    return ChatOllama(model="llama3")


# Function to generate an answer to a given query
def generate_answer(query):
    context = ""  # Initialize an empty context string

    # Retrieve relevant context chunks (documents) for the given query
    for document in rt.get_context_chunks(query):
        # If the document is a list and contains content in its first element, join its page content
        if isinstance(document, list) and document[0].page_content:
            context = "\n".join(document[0].page_content)
        else:
            # Otherwise, directly append the document's page content
            context += document.page_content

    # Construct the prompt for the language model using the retrieved context and the original query
    prompt = f"Answer the question based on the following context:\n\n{context}\n\nQuestion: {query}\nAnswer:"

    # Invoke the model with the prompt and return the result
    return get_chat_model().invoke(prompt)