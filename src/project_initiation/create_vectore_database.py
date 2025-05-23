import os
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
# ...rest of your code...
# Set paths
documents_dir = "./knowledge/"
vector_db_dir = "./db/"

def create_vector_database():
    # 1. Load documents from the directory
    loader = DirectoryLoader(documents_dir)
    documents = loader.load()
    print(f"Loaded {len(documents)} documents")
    
    # 2. Split documents into smaller chunks for better processing
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,        # Each chunk will have ~500 characters
        chunk_overlap=50       # Overlap between chunks to maintain context
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split into {len(chunks)} chunks")
    
    # 3. Create embeddings using a local model (no API key needed)
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"  # A small, efficient embedding model
    )
    
    # 4. Create and save the vector database locally
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=vector_db_dir
    )
    
    # 5. Persist the database to disk
    vector_db.persist()
    print(f"Vector database created and saved to {vector_db_dir}")
    
    return vector_db