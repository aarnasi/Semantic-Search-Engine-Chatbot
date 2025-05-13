from langchain_text_splitters import RecursiveCharacterTextSplitter


# Function to split a given text (as documents) into manageable chunks
def get_chunked_text(text):
    # Initialize the text splitter with specified chunk size and overlap
    # - chunk_size: maximum number of characters per chunk
    # - chunk_overlap: number of overlapping characters between chunks
    # - add_start_index: adds metadata indicating where each chunk starts in the original text
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, add_start_index=True
    )

    # Split the input text (assumed to be a list of Document objects) into chunks
    return text_splitter.split_documents(text)