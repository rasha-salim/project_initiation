import sys
print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")

print("\nChecking if crewai is installed:")
try:
    import crewai
    print("CrewAI is installed!")
    print(f"CrewAI version: {crewai.__version__}")
except ImportError as e:
    print(f"CrewAI is not installed: {e}")

print("\nChecking if langchain packages are installed:")
try:
    import langchain_community
    print("langchain_community is installed!")
except ImportError as e:
    print(f"langchain_community is not installed: {e}")

try:
    import langchain_core
    print("langchain_core is installed!")
except ImportError as e:
    print(f"langchain_core is not installed: {e}")
