from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import streamlit as st


# websearch agent
websearch_agent=Agent(
    name='Web Search Agent',
    role='Search the web for the information',
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=['Always include sourcess'],
    show_tool_calls=True,
    markdown=True,
)


# financial agent
finance_agent=Agent(
    name= 'Finance AI Agent',
    model=Groq(id='llama3-groq-70b-8192-tool-use-preview'),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)
    ],
    instructions=['Use tables to display the data'],
    show_tool_calls=True,
    markdown=True

)


multi_ai_agent=Agent(
    team=[websearch_agent,finance_agent],
    instructions=['Always include sources', 'Use table to display the data'],
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent.print_response('Summarise analyst recommendation and share the latest news for NVDA', stream=True)


# txt = st.text_area( 'ask....')
