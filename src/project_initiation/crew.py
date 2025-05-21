from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from langchain_anthropic import ChatAnthropic
import os
from .output import ProjectScopeDocument, ProductRoadmap

from langchain.output_parsers import PydanticOutputParser
from crewai_tools import (FileReadTool)
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

# include the knowledge sources you want to use in your crew
project_brief_path = "C:/Users/rasha/project_initiation/knowledge/Project_brief.md"
meeting_transcript_path = "C:/Users/rasha/project_initiation/knowledge/prekickoff_transcript.md"

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

project_brief_tool = SafeFileReadTool(
    name="Project Brief",
    description="Project Brief document",
    file_path=project_brief_path,
    start_line=0,        # Add default starting line
    line_count=-1)        # -1 could indicate "read all lines"



meeting_transcript_tool = SafeFileReadTool(
    name="Meeting Transcript",
    description="Meeting Transcript document",
    file_path=meeting_transcript_path,
     start_line=0,        # Add default starting line
    line_count=-1)        # -1 could indicate "read all lines"

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
            tools=[project_brief_tool, meeting_transcript_tool],
            human_input=True,
        )

    @agent
    def technical_lead_scope_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['technical_lead_scope_specialist'], # type: ignore[index]
            verbose=True,
            llm=self.llm,
            allow_delegation=True,
            delegation_timeout=60
        )
    
    @agent
    def chief_product_officer(self) -> Agent:
        return Agent(
            config=self.agents_config['chief_product_officer'], # type: ignore[index]
            verbose=True,
            allow_delegation=True,
            delegation_timeout=60,
            llm=self.llm,
            allow_human_input=True
        )
    
    @agent
    def product_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['product_manager'], # type: ignore[index]
            verbose=True,
            llm=self.llm,
            allow_delegation=True,
            delegation_timeout=60

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
             output_file='project_scope.json'
        )
    
    @task
    def technical_sections_expansion(self) -> Task:
        return Task(
            config=self.tasks_config['technical_sections_expansion'], # type: ignore[index]
            output_pydantic= ProjectScopeDocument,
            output_parser= self.project_scope_parser,
        
        )
    
    @task
    def review_and_approval(self) -> Task:
        return Task(
            config=self.tasks_config['review_and_approval'], # type: ignore[index]
            output_pydantic= ProjectScopeDocument,
            output_parser= self.project_scope_parser,
            output_file='project_scope.json'
        )

    
    @task
    def roadmap_development(self) -> Task:
        return Task(
            config=self.tasks_config['roadmap_development'], # type: ignore[index]
            output_pydantic= ProjectScopeDocument,
             output_parser= self.Project_roadmap_parser,
             output_file='project_roadmap.json'
        )
    
   

    @crew
    def crew(self) -> Crew:
        """Creates the ProjectInitiation crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

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
