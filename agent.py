from langchain.agents import AgentType, initialize_agent
from llm import llm
from graph import graph
from promptlib import receptionist
from langchain.chains.conversation.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True,
)

tools = []

agent = initialize_agent(
    tools,
    llm,
    memory=memory,
    verbose=True,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    agent_kwargs={"system_message": receptionist}
)

def generate_response(prompt):
    response = agent(prompt)
    return response['output']