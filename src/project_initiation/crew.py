from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List, Dict
from langchain_anthropic import ChatAnthropic
import os
from .output import ProjectScopeDocument, ProductRoadmap
from langchain.output_parsers import PydanticOutputParser
from .tools.custom_tool import (SafeFileReadTool, KnowledgeSearchTool)
from .rag_utils import RAGContextRetriever
from .task_context_provider import TaskContextProvider
from src.project_initiation.create_vectore_database import create_vector_database


#TODO#1:
# 1. Embed the documents and store them in a vector database
# 2. Use the vector database to retrieve the documents
# 3. Pass the retrieved documents to the agents

#TODO#2:
# 1. Add the roadmap visualization tool, agent, and task
# 2. Add the project scope visualization tool, agent, and task

#TODO#3:
# 1. Deploy te crew
# 2. Create the app to run the crew

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

# include the knowledge sources you want to use in your crew
project_brief_path = "C:/Users/rasha/project_initiation/knowledge/Project_brief.md"
meeting_transcript_path = "C:/Users/rasha/project_initiation/knowledge/prekickoff_transcript.md"

knowledge_tool = KnowledgeSearchTool()

@CrewBase
class ProjectInitiation():
    
    # In your crew initialization
    llm = ChatAnthropic(model="claude-3-haiku-20240307",                        
                    anthropic_api_key=os.environ.get("ANTHROPIC_API_KEY"),
                    max_tokens=4096)
    """ProjectInitiation crew"""

    # Create the parser
    project_scope_parser = PydanticOutputParser(pydantic_object=ProjectScopeDocument)
    Project_roadmap_parser = PydanticOutputParser(pydantic_object=ProductRoadmap)

    agents: List[BaseAgent]
    tasks: List[Task]
    
    # Store enhanced tasks
    _enhanced_tasks: Dict[str, Task] = {}
    
    # RAG components
    rag_retriever: RAGContextRetriever = None
    task_context_provider: TaskContextProvider = None
    
    def initialize_rag_pipeline(self):
        """Initialize the RAG pipeline before the crew starts"""
        print("Initializing RAG pipeline...")
        
        # Create or ensure the vector database exists
        try:
            create_vector_database()
            print("Vector database created/updated successfully")
        except Exception as e:
            print(f"Warning: Error creating vector database: {str(e)}")
            print("Continuing with existing vector database if available")
        
        # Initialize RAG components
        self.rag_retriever = RAGContextRetriever()
        self.task_context_provider = TaskContextProvider(self.rag_retriever)
        
        # Only enhance tasks if they exist (might not be initialized during testing)
        if hasattr(self, 'tasks') and self.tasks:
            print("Enhancing tasks with RAG context...")
            # Map tasks to agent roles for context enhancement
            task_agent_roles = {
                "document_analysis": "business_analyst",
                "scope_development": "product_manager",
                "technical_sections_expansion": "technical_lead_scope_specialist",
                "review_and_approval": "chief_product_officer",
                "roadmap_development": "product_manager"
            }
            
            # Enhance tasks with RAG context
            task_dict = {task.id: task for task in self.tasks}
            self._enhanced_tasks = self.task_context_provider.enhance_tasks(task_dict, task_agent_roles)
            
            # Replace original tasks with enhanced tasks
            for i, task in enumerate(self.tasks):
                if task.id in self._enhanced_tasks:
                    self.tasks[i] = self._enhanced_tasks[task.id]
            print("Tasks enhanced with context from the RAG pipeline")
        else:
            print("No tasks to enhance yet - RAG pipeline is ready for when tasks are created")
        
        print("RAG pipeline initialization complete")

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

    @agent
    def business_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['business_analyst'], # type: ignore[index]
            verbose=True,
            llm=self.llm, 
            tools=[knowledge_tool]
        )

    @agent
    def technical_lead_scope_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['technical_lead_scope_specialist'], # type: ignore[index]
            verbose=True,
            llm=self.llm,
            allow_delegation=True,
            delegation_timeout=60,
            tools=[knowledge_tool]
        )
    
    @agent
    def chief_product_officer(self) -> Agent:
        return Agent(
            config=self.agents_config['chief_product_officer'], # type: ignore[index]
            verbose=True,
            allow_delegation=True,
            delegation_timeout=60,
            llm=self.llm,
            tools=[knowledge_tool]
        )
    
    @agent
    def product_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['product_manager'], # type: ignore[index]
            verbose=True,
            llm=self.llm,
            allow_delegation=True,
            delegation_timeout=60,
            tools=[knowledge_tool]
        )
    
    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def document_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['document_analysis'], # type: ignore[index]
            
        )

    @task
    def scope_development(self) -> Task:
        return Task(
            config=self.tasks_config['scope_development'], # type: ignore[index]
            output_pydantic= ProjectScopeDocument,
            output_parser= self.project_scope_parser,
            output_file='project_scope_vdb.json',
            human_input=True
        )
    
    @task
    def technical_sections_expansion(self) -> Task:
        return Task(
            config=self.tasks_config['technical_sections_expansion'], # type: ignore[index]
            output_pydantic= ProjectScopeDocument,
            output_parser= self.project_scope_parser,
            human_input=True
        
        )
    
    @task
    def review_and_approval(self) -> Task:
        return Task(
            config=self.tasks_config['review_and_approval'], # type: ignore[index]
            output_pydantic= ProjectScopeDocument,
            output_parser= self.project_scope_parser,
            output_file='./output/project_scope_vdb.json',
            human_input=True
        )

    
    @task
    def roadmap_development(self) -> Task:
        return Task(
            config=self.tasks_config['roadmap_development'], # type: ignore[index]
            output_pydantic= ProjectScopeDocument,
             output_parser= self.Project_roadmap_parser,
             output_file='./output/project_roadmap.json',
             human_input=True
        )
    
   

    @crew
    def crew(self) -> Crew:
        """Creates the ProjectInitiation crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        # Initialize the RAG pipeline before creating the crew
        self.initialize_rag_pipeline()
        
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            retry_on_failure=True, # Retry the crew if it fails
            max_rpm=50, # Maximum requests per minute
            retry_attempts=5, # Number of retry attempts
            retry_wait_time=10, # Wait time between retry attempts
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
