from langchain.agents import AgentType, initialize_agent
from llm import llm

agent = initialize_agent(
    tools,
    llm,
    memory=memory,
    verbose=True,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
)