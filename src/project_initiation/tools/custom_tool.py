from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from crewai_tools import (FileReadTool)
import os
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.tools import Tool
from langchain.schema import Document

# Create a custom wrapper for FileReadTool
class SafeFileReadTool(FileReadTool):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def _run(self, file_path=None, start_line=None, line_count=None, **kwargs):
        # Sanitize inputs
        file_path = file_path or self.file_path
        start_line = 0 if start_line is None else start_line
        line_count = -1 if line_count is None else line_count
        
        # Call the parent method with sanitized values
        return super()._run(file_path=file_path, start_line=start_line, line_count=line_count, **kwargs)
    

class KnowledgeSearchTool(BaseTool):
    name: str = "Knowledge Search"
    description: str = "Search the company knowledge base for relevant information"

    def __init__(self):
        super().__init__()
        self._vector_db = None  # Cache the vector database


    def load_vector_database(self):
        """Load and cache the vector database"""
        if self._vector_db is None:
            try:
                embeddings = HuggingFaceEmbeddings(
                    model_name="all-MiniLM-L6-v2"
                )
                self._vector_db = Chroma(
                    persist_directory="./db/",
                    embedding_function=embeddings
                )
            except Exception as e:
                return None, f"Error loading vector database: {str(e)}"
        return self._vector_db, None

    def _run(self, query: str) -> str:
        """Search the knowledge base for relevant information"""
        vector_db, error = self.load_vector_database()
        
        if error:
            return f"Error: {error}"
        
        if vector_db is None:
            return "Error: Could not load vector database."
        
        try:
            docs = vector_db.similarity_search(query, k=3)
            if docs:
                combined_info = "\n\n".join([doc.page_content for doc in docs])
                return f"Relevant information found:\n\n{combined_info}"
            else:
                return "No relevant information found in the knowledge base."
        except Exception as e:
            return f"Error during search: {str(e)}"
        

    

class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."
