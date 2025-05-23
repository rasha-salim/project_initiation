"""
Test script for the RAG pipeline components only
This script tests only the RAG components without initializing the CrewAI class
"""
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Test the RAG retriever
from src.project_initiation.rag_utils import RAGContextRetriever
from src.project_initiation.task_context_provider import TaskContextProvider
from crewai import Task

def main():
    print("Testing RAG pipeline components...\n")
    
    # Test the RAG retriever directly
    print("1. Testing RAG retriever...")
    rag = RAGContextRetriever()
    context = rag.format_context_for_task("project requirements")
    print(f"Retrieved context sample: {context[:150]}...\n")
    
    # Test the task context provider
    print("2. Testing task context provider...")
    task_provider = TaskContextProvider(rag)
    sample_task = Task(
        description="Analyze the project requirements and create a comprehensive scope document",
        expected_output="A detailed project scope document"
    )
    enhanced_task = task_provider.enhance_task_with_context(sample_task, "business_analyst")
    print(f"Enhanced task description sample: {enhanced_task.description[:150]}...\n")
    
    print("RAG pipeline components test completed successfully!")
    print("Your RAG pipeline is ready to be integrated with CrewAI.")
    print("When you run your crew, make sure to call initialize_rag_pipeline() before creating the Crew instance.")

if __name__ == "__main__":
    main()
