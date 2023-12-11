import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings

llm=ChatOpenAI
embeddings=OpenAIEmbeddings