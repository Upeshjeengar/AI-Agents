'''
from google.adk.tools import google_search
root_agent = Agent(
    name="helpful_assistant",
    model="gemini-2.5-flash-lite",
    description="A simple agent that can answer general questions.",
    instruction="You are a helpful assistant. Use Google Search for current info or if unsure.",
    tools=[google_search],
)
'''
import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
import os
from google.adk.models.lite_llm import LiteLlm
from ddgs import DDGS
# from dotenv import load_dotenv
# load_dotenv()
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def google_search(query: str) -> dict:
    """Performs a Google search for the given query and returns the top result.

    Args:
        query (str): The search query.
    """
    try:
        results=DDGS().text(query, max_results=3)
        if not results:
            return {
                "status": "error",
                "error_message": f"No results found for query: {query}",
            }

        report_snippets = []
        for i,res in enumerate(results):
            report_snippets.append(f"Source {i+1} ({res['href']}):\n{res['body']}")
        report = "\n\n".join(report_snippets)
        return {"status": "success", "report": report}
    except Exception as e:
        return {"status": "error", "error_message": f"Search failed: {str(e)}"}

def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (77 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}

model = LiteLlm(
    model = "openai/llama3.1",
    api_key = "ollama",
    base_url = "http://localhost:11434/v1"  # This is the missing piece
)

root_agent = Agent(
    name="helpful_agent",
    model=model,
    
    description=(
        "Agent to answer questions from internet and the time and weather in a city."
    ),
    instruction=(
        "You are a helpful agent. You must follow these rules strictly:\n"
        "1. For any user question about general knowledge, facts, current events, or any topic that is not about time or weather, use the `Google Search` tool.\n"
        "2. For user questions specifically about the weather in a city, you MUST use the `get_weather` tool.\n"
        "3. For user questions specifically about the current time in a city, you MUST use the `get_current_time` tool.\n"
        "4. If 'get_weather' or 'get_current_time' tool returned an error message about the requested city, then you must use 'google_search' tool"
        "5. If a tool returns an error, apologize and report the error message to the user."
    ),
    tools=[get_weather, get_current_time,google_search],

    max_iterations=3,
)