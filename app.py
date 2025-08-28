from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

os.environ["GOOGLE_API_KEY"]   = os.getenv("GOOGLE_API_KEY") 

# lang smith
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

prompt =ChatPromptTemplate.from_messages( [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ])


st.title('Langchain chatbot With GOOGLE API')
input_text=st.text_input("Search the topic u want")


output = StrOutputParser()
chain = prompt|llm|output

if input_text:
    st.write(chain.invoke({"question":input_text}))



