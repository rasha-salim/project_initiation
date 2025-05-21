from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from langchain_anthropic import ChatAnthropic
import os
from output import ProjectScopeDocument, ProductRoadmap
from langchain.output_parsers import PydanticOutputParser
from crewai_tools import (FileReadTool)
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

# include the knowledge sources you want to use in your crew
research_analysis_path = os.path.join(os.path.dirname(__file__), 'knowledge', 'Phase1_Research_&_Analysis_Report_SmartAssist-document.docx') 
project_brief_path = os.path.join(os.path.dirname(__file__), 'knowledge', 'Project_Brief_SmartAssist_Internal_LLM_Solution_document.docx')
meeting_notes_path = os.path.join(os.path.dirname(__file__), 'knowledge', 'SmartAssist_Mtg_Notes_May1.docx')
meeting_transcript_path = os.path.join(os.path.dirname(__file__), 'knowledge', 'TechNova_x_AI_Solutions_SmartAssist_PreKickoff_Call_Transcript.docx')

project_brief_tool = FileReadTool(
    name="Project Brief",
    description="Project Brief document",
    file_path=project_brief_path,
    file_type="docx",
    file_content="Project Brief document content")

meeting_notes_tool = FileReadTool(
    name="Meeting Notes",
    description="Meeting Notes document",
    file_path=meeting_notes_path,
    file_type="docx",
    file_content="Meeting Notes document content")

meeting_transcript_tool = FileReadTool(
    name="Meeting Transcript",
    description="Meeting Transcript document",
    file_path=meeting_transcript_path,
    file_type="docx",
    file_content="Meeting Transcript document content") 

research_analysis_tool = FileReadTool(
    name="Research Analysis",
    description="Research Analysis document",
    file_path=research_analysis_path,
    file_type="docx",
    file_content="Research Analysis document content")

@CrewBase
class ProjectInitiation():
    
    # In your crew initialization
    llm = ChatAnthropic(model="claude-3-haiku-20240307",                        
                    anthropic_api_key=os.environ.get("ANTHROPIC_API_KEY"))
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
            llm=self.llm
        )

    @agent
    def technical_lead_scope_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['technical_lead_scope_specialist'], # type: ignore[index]
            verbose=True,
            llm=self.llm
        )
    
    @agent
    def chief_product_officer(self) -> Agent:
        return Agent(
            config=self.agents_config['chief_product_officer'], # type: ignore[index]
            verbose=True,
            llm=self.llm
        )
    
    @agent
    def product_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['product_manager'], # type: ignore[index]
            verbose=True,
            llm=self.llm
        )
    
    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def document_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['document_analysis'], # type: ignore[index]
            output_pydantic= ProjectScopeDocument,
            
        )

    @task
    def scope_development(self) -> Task:
        return Task(
            config=self.tasks_config['section_development'], # type: ignore[index]
            output_pydantic= ProjectScopeDocument,
             output_parser= self.project_scope_parser,
             agents=[self.technical_lead_scope_specialist], # type: ignore[index]
             context=[self.document_analysis], # type: ignore[index]
        )
    
    @task
    def technical_sections_expansion(self) -> Task:
        return Task(
            config=self.tasks_config['technical_sections_expansion'], # type: ignore[index]
            output_pydantic= ProjectScopeDocument,
            output_parser= self.project_scope_parser,
            context=[self.scope_development], # type: ignore[index]
        
        )
    

    @task
    def final_review_and_approval(self) -> Task:
        return Task(
            config=self.tasks_config['document_aggregation'], # type: ignore[index]
            output_pydantic= ProjectScopeDocument,
            output_parser= self.project_scope_parser,
            agents=[self.chief_product_officer], # type: ignore[index]
            dependencies=[self.roadmap_development, self.scope_document_compilation], # type: ignore[index]
             output_file='project_scope.json'
        )

    
    @task
    def roadmap_development(self) -> Task:
        return Task(
            config=self.tasks_config['roadmap_development'], # type: ignore[index]
            output_pydantic= ProjectScopeDocument,
             output_parser= self.Project_roadmap_parser,
             output_file='project_scope.json',
             agents=[self.product_manager], # type: ignore[index]
             context=[self.technical_sections_expansion] # type: ignore[index]
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
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
