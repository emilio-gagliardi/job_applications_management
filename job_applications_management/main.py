# from langtrace_python_sdk import langtrace
import os
from app_utils import (
    get_openai_api_key,
    get_exa_api_key,
    get_serper_api_key,
)

from crewai import Agent, Task, Crew


os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo"
os.environ["OPENAI_API_KEY"] = get_openai_api_key()
os.environ["EXA_API_KEY"] = get_exa_api_key()
os.environ["SERPER_API_KEY"] = get_serper_api_key()


def test_crew_framework():

    # Define the agent
    agent = Agent(
        role="Greeter",
        goal="Greet the world",
        backstory="You are a friendly AI that loves to greet people.",
    )

    # Define the task
    task = Task(
        description="Print 'Successfully loaded:\nEnvironment variables\nAgent class instance\nTask class instance\nCrew class instance.\nInitial dockerization working.'",
        expected_output="a cheerful message.",
        agent=agent,
    )

    # Create the crew
    crew = Crew(agents=[agent], tasks=[task])

    # Run the crew
    result = crew.kickoff()

    print(result)


if __name__ == "__main__":
    test_crew_framework()
