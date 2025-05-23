# Project Initiation

Welcome to the Project Initiation repository! This project provides a template for setting up a multi-agent AI system using [crewAI](https://crewai.com). The goal is to help you quickly configure, customize, and launch collaborative AI agents for complex workflows.

## Installation

**Requirements:**  
- Python >=3.10, <3.13  
- [UV](https://docs.astral.sh/uv/) for dependency management

**Steps:**

1. Install UV (if not already installed):

    ```bash
    pip install uv
    ```

2. Navigate to your project directory and install dependencies:

    ```bash
    crewai install
    ```

## Configuration

1. Add your `OPENAI_API_KEY` to the `.env` file.
2. Edit agent and task configurations:
    - `src/project_initiation/config/agents.yaml` — define your agents
    - `src/project_initiation/config/tasks.yaml` — define your tasks
3. Customize logic, tools, and arguments in:
    - `src/project_initiation/crew.py`
    - `src/project_initiation/main.py` (for custom agent/task inputs)

## Usage

To launch your AI crew and execute tasks, run:

```bash
crewai run
```

This will initialize your agents and assign tasks as specified in your configuration files. By default, the project generates a `project_roadmap.json` and `project_scope.json` in the root directory containing the results of your configured tasks.

## Project Structure

- **Agents:** Defined in `config/agents.yaml` with unique roles and capabilities.
- **Tasks:** Outlined in `config/tasks.yaml` for collaborative execution.
- **Logic & Tools:** Extend or modify in `crew.py` and `main.py` as needed.

## Support

- [Documentation](https://docs.crewai.com)
- [GitHub Issues](https://github.com/joaomdmoura/crewai)
- [Discord Community](https://discord.com/invite/X4JWnZnxPb)
- [Docs Chat](https://chatg.pt/DWjSBZn)

Empower your workflows with collaborative AI agents using crewAI!
