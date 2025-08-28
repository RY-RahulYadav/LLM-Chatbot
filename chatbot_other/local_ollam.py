from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama


import os
import streamlit as st
from dotenv import load_dotenv


load_dotenv()

# lang smith
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")

llm = Ollama(model="llama2")

prompt =ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "Question:{question}")
])

st.title("Chatbot")
input_text = st.text_input("Enter your message")


output = StrOutputParser()
chain = prompt|llm|output

if input_text:
    st.write(chain.invoke({"question":input_text}))



