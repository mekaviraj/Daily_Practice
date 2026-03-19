# from phi.agent import Agent
# from phi.model.groq import Groq
# from phi.tools.yfinance import YFinanceTools
# from phi.tools.duckduckgo import DuckDuckGo
# import openai

# from dotenv import load_dotenv
# load_dotenv()

# import os
# openai.api_keys = os.getenv("OPENAI_API_KEY")
# # web search agent
# web_search_agent = Agent(
#     name="web search agent",
#     role="search the web for the information",
#     model=Groq(id="llama-3.1-8b-instant"),
#     tools=[DuckDuckGo()],
#     instructions=["always include sources"],
#     show_tool_calls=True,
#     markdown=True,
# )

# # Financial agent
# finance_agent = Agent(
#     name="Finance AI Agent",
#     model=Groq(id="llama-3.1-8b-instant"),
#     tools=[
#         YFinanceTools(
#             stock_price=True,
#             analyst_recommendations=True,
#             stock_fundamentals=True,
#             company_news=True,
#         ),
#     ],
#     instructions=["Use tables to display the data"],
#     show_tool_calls=True,
#     markdown=True,
# )

# # Multi-agent system
# # multi_ai_agent = Agent(
# #     team=[web_search_agent, finance_agent],
# #     instructions=["Always include sources", "Use table to display the data"],
# #     show_tool_calls=True,
# #     markdown=True,
# # )

# multi_ai_agent = Agent(
#     team=[web_search_agent, finance_agent],
#     model=Groq(id="llama-3.1-8b-instant"),   # ✅ THIS IS THE KEY FIX
#     instructions=["Always include sources", "Use table to display the data"],
#     show_tool_calls=True,
#     markdown=True,
# )

# multi_ai_agent.print_response(
#     "Summarize analyst recommendation and share the latest news for NVDA",
#     stream=True,
# )
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

# Single powerful agent (NO multi-agent bugs)
agent = Agent(
    name="Finance + Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        DuckDuckGo(),   # for news/search
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True,
        ),
    ],
    instructions=[
        "Summarize clearly",
        "Always include sources for news",
        "Use tables for financial data",
    ],
    show_tool_calls=True,
    markdown=True,
)

# Run query
agent.print_response(
    "Summarize analyst recommendation and share latest news for NVDA",
    stream=True,
)