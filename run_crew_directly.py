"""
Script to run the CrewAI project directly using Python
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import the ProjectInitiation class
from src.project_initiation.crew import ProjectInitiation

def main():
    print("Initializing ProjectInitiation crew...")
    
    # Create the crew instance
    project_crew = ProjectInitiation()
    
    # Get the crew instance (this will initialize the RAG pipeline)
    crew_instance = project_crew.crew()
    
    print("Running the crew...")
    # Run the crew
    result = crew_instance.kickoff()
    
    print("Crew execution completed!")
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
