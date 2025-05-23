from crewai import Task
from .rag_utils import RAGContextRetriever
from typing import Optional, Dict, Any

class TaskContextProvider:
    """
    A utility class that enhances CrewAI tasks with context from the RAG system.
    This class wraps tasks and injects relevant context from the vector database
    before they are executed.
    """
    
    def __init__(self, rag_retriever: Optional[RAGContextRetriever] = None):
        """
        Initialize the task context provider.
        
        Args:
            rag_retriever: An instance of RAGContextRetriever to use for context retrieval
        """
        self.rag_retriever = rag_retriever or RAGContextRetriever()
    
    def enhance_task_with_context(self, task: Task, agent_role: str) -> Task:
        """
        Enhance a task with context from the RAG system.
        
        Args:
            task: The CrewAI task to enhance
            agent_role: The role of the agent that will execute the task
            
        Returns:
            The enhanced task with context
        """
        # Get the original description
        original_description = task.description
        
        # Retrieve context for this task and agent
        context = self.rag_retriever.get_context_for_agent(
            agent_role=agent_role,
            task_description=original_description
        )
        
        # Create an enhanced description with the context
        enhanced_description = f"""
{original_description}

RELEVANT CONTEXT FROM KNOWLEDGE BASE:
{context}

Use the above context to help you complete this task. You can also use the Knowledge Search tool if you need more information.
"""
        
        # Create a new task with the enhanced description
        # Get task attributes safely
        task_args = {
            "description": enhanced_description,
            "expected_output": getattr(task, "expected_output", None),
            "agent": getattr(task, "agent", None),
            "human_input": getattr(task, "human_input", False),
            "async_execution": getattr(task, "async_execution", False),
        }
        
        # Add optional attributes if they exist
        if hasattr(task, "output_file"):
            task_args["output_file"] = task.output_file
        if hasattr(task, "output_pydantic"):
            task_args["output_pydantic"] = task.output_pydantic
        if hasattr(task, "output_parser"):
            task_args["output_parser"] = task.output_parser
        if hasattr(task, "callback"):
            task_args["callback"] = task.callback
        if hasattr(task, "context"):
            task_args["context"] = task.context
            
        # Create the enhanced task
        enhanced_task = Task(**task_args)
        
        return enhanced_task
    
    def enhance_tasks(self, tasks: Dict[str, Task], agent_roles: Dict[str, str]) -> Dict[str, Task]:
        """
        Enhance multiple tasks with context.
        
        Args:
            tasks: Dictionary mapping task names to Task objects
            agent_roles: Dictionary mapping task names to agent roles
            
        Returns:
            Dictionary of enhanced tasks
        """
        enhanced_tasks = {}
        
        for task_name, task in tasks.items():
            agent_role = agent_roles.get(task_name, "general")
            enhanced_tasks[task_name] = self.enhance_task_with_context(task, agent_role)
        
        return enhanced_tasks
