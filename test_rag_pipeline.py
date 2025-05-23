"""
Test script for the RAG pipeline integration with CrewAI
"""
import os
import sys
from src.project_initiation.rag_utils import RAGContextRetriever
from src.project_initiation.task_context_provider import TaskContextProvider
from crewai import Task, Agent

# Initialize the RAG components
rag_retriever = RAGContextRetriever()
task_context_provider = TaskContextProvider(rag_retriever)

# Test RAG retrieval
print("Testing RAG retrieval...")
context = rag_retriever.format_context_for_task("project requirements")
print(f"Retrieved context: {context[:200]}...\n")

# Create a sample task
print("Testing task enhancement with RAG context...")
sample_task = Task(
    description="Analyze the project requirements and create a comprehensive scope document",
    expected_output="A detailed project scope document"
)

# Enhance the task with context
enhanced_task = task_context_provider.enhance_task_with_context(
    task=sample_task,
    agent_role="business_analyst"
)

# Print the original and enhanced descriptions
print(f"Original task description: {sample_task.description}")
print(f"Enhanced task description (first 200 chars): {enhanced_task.description[:200]}...\n")

print("RAG pipeline test completed successfully!")
