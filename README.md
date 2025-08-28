# Chatbot Project

This repository contains a simple chatbot application built using Streamlit and LangChain, supporting multiple LLM backends (Google Gemini, OpenAI, and Ollama).

## Folder Structure

- `app.py`: Main Streamlit app using Google Gemini API via LangChain.
- `requirements.txt`: Python dependencies for the project.
- `chatbot_other/`
  - `chatbot_using_openai.py`: Streamlit chatbot using OpenAI's GPT-3.5 Turbo via LangChain.
  - `local_ollam.py`: Streamlit chatbot using Ollama (Llama2 model) via LangChain.

## Features
- Modular chatbot implementations for different LLM providers.
- Uses environment variables for API keys (see `.env` file).
- Simple Streamlit UI for user interaction.
- LangSmith tracing enabled for debugging and analytics.

## Setup Instructions

1. **Clone the repository**
2. **Create a `.env` file** with your API keys:
   ```env
   GOOGLE_API_KEY=your_google_api_key
   LANGSMITH_API_KEY=your_langsmith_api_key
   CHAT_OPEN_API=your_openai_api_key
   ```
3. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```
4. **Run the chatbot app**:
   - For Google Gemini:
     ```powershell
     streamlit run app.py
     ```
   - For OpenAI:
     ```powershell
     streamlit run chatbot_other/chatbot_using_openai.py
     ```
   - For Ollama (Llama2):
     ```powershell
     streamlit run chatbot_other/local_ollam.py
     ```

## Requirements
- Python 3.8+
- Streamlit
- LangChain
- API keys for Google Gemini, OpenAI, and/or Ollama

## License
MIT

## Author
Rahul Yadav
