import streamlit as st
from utils import write_message
from agent import generate_response

st.set_page_config("WiGPTia", page_icon="🦾")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome to WiGPTia, the front desk of our GPT warehouse.  How can I help you?"},
    ]

def handle_submit(message):
    with st.spinner('Browsing indexed GPTs...'):

        response = generate_response(message)
        write_message('assistant', response)

with st.container():
    for message in st.session_state.messages:
        write_message(message['role'], message['content'], save=False)

    if prompt := st.chat_input("Type in your question or the task you need help with"):# Display user message in chat message container
        write_message('user', prompt)# Generate a response
        handle_submit(prompt)