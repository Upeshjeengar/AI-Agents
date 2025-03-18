from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.openai import OpenAI
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools

load_dotenv()

web_agent=Agent(
    name="Web Agent",
    role="Get web data",
    model=OpenAI(id="gpt-4o"),
    tools=[DuckDuckGo()],
    instructions="Always include sources",
    markdown=True,
    show_tool_calls=True
)

#We are using LLM which does'nt have access to internet so we will use yfinance to get the data
finance_agent=Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAI(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,stock_fundamentals=True)],
    instructions="Use table to display the data",
    show_tool_calls=True,
    markdown=True,
)

agent_team=Agent(
    team=[web_agent,finance_agent],
    instructions=["Always include sources","Use table to display the data"],
    show_tool_calls=True,
    markdown=True,
)
agent_team.print_response("Summarize and compare analyst recommendations for TSLA and NVDA")
