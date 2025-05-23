from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document
from typing import List, Dict, Any, Optional

class RAGContextRetriever:
    """
    Utility class for retrieving context from the vector database for CrewAI agents.
    This class provides methods to retrieve relevant context based on queries and
    format it for use in CrewAI tasks.
    """
    
    def __init__(self, persist_directory: str = "./db/", 
                 model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize the RAG context retriever.
        
        Args:
            persist_directory: Directory where the vector database is stored
            model_name: Name of the embedding model to use
        """
        self._vector_db = None
        self.persist_directory = persist_directory
        self.model_name = model_name
    
    def _load_vector_db(self) -> Optional[Chroma]:
        """
        Load the vector database if it's not already loaded.
        
        Returns:
            The loaded vector database or None if there was an error
        """
        if self._vector_db is None:
            try:
                embeddings = HuggingFaceEmbeddings(
                    model_name=self.model_name
                )
                self._vector_db = Chroma(
                    persist_directory=self.persist_directory,
                    embedding_function=embeddings
                )
            except Exception as e:
                print(f"Error loading vector database: {str(e)}")
                return None
        return self._vector_db
    
    def retrieve_context(self, query: str, k: int = 3) -> List[Document]:
        """
        Retrieve relevant documents from the vector database based on a query.
        
        Args:
            query: The query to search for
            k: Number of documents to retrieve
            
        Returns:
            List of retrieved documents
        """
        vector_db = self._load_vector_db()
        if vector_db is None:
            return []
        
        try:
            docs = vector_db.similarity_search(query, k=k)
            return docs
        except Exception as e:
            print(f"Error during search: {str(e)}")
            return []
    
    def format_context_for_task(self, query: str, k: int = 3) -> str:
        """
        Format retrieved context as a string for use in CrewAI tasks.
        
        Args:
            query: The query to search for
            k: Number of documents to retrieve
            
        Returns:
            Formatted context string
        """
        docs = self.retrieve_context(query, k)
        if not docs:
            return "No relevant information found in the knowledge base."
        
        # Format the documents into a single string
        context_parts = []
        for i, doc in enumerate(docs, 1):
            source = getattr(doc.metadata, 'source', 'Unknown source')
            context_parts.append(f"Document {i} (Source: {source}):\n{doc.page_content}\n")
        
        return "\n".join(context_parts)
    
    def get_context_for_agent(self, agent_role: str, task_description: str) -> str:
        """
        Get context specifically tailored for an agent's role and task.
        
        Args:
            agent_role: The role of the agent (e.g., "business_analyst")
            task_description: Description of the task the agent is performing
            
        Returns:
            Context tailored for the agent and task
        """
        # Create a query that combines the agent role and task description
        query = f"{agent_role} needs to {task_description}"
        
        # Retrieve and format context
        return self.format_context_for_task(query)
