"""
Test script for the CrewAI RAG pipeline integration
"""
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from src.project_initiation.crew import ProjectInitiation

def main():
    print("Testing RAG pipeline components...")
    
    # Test the RAG retriever directly
    from src.project_initiation.rag_utils import RAGContextRetriever
    print("\n1. Testing RAG retriever...")
    rag = RAGContextRetriever()
    context = rag.format_context_for_task("project requirements")
    print(f"Retrieved context sample: {context[:150]}...\n")
    
    # Test the task context provider
    from src.project_initiation.task_context_provider import TaskContextProvider
    from crewai import Task
    print("2. Testing task context provider...")
    task_provider = TaskContextProvider(rag)
    sample_task = Task(
        description="Analyze the project requirements and create a comprehensive scope document",
        expected_output="A detailed project scope document"
    )
    enhanced_task = task_provider.enhance_task_with_context(sample_task, "business_analyst")
    print(f"Enhanced task description sample: {enhanced_task.description[:150]}...\n")
    
    # Initialize the RAG pipeline in the CrewAI class
    print("3. Testing RAG pipeline initialization in CrewAI class...")
    project_crew = ProjectInitiation()
    project_crew.initialize_rag_pipeline()
    
    print("\nRAG pipeline integration test completed successfully!")
    print("Your CrewAI agents now have access to the knowledge base through the RAG pipeline.")
    print("When you run your crew, the tasks will be automatically enhanced with relevant context.")

if __name__ == "__main__":
    main()
