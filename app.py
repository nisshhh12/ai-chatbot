import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Streamlit App
st.set_page_config(page_title="Gemini Chatbot", layout="wide")
st.title("💬 Gemini 2.0 Flash Chatbot")

# Session State Initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="You are a helpful assistant.")]
if "chat_display" not in st.session_state:
    st.session_state.chat_display = []

# Input box
user_input = st.chat_input("Say something to the bot...")

# If user types something
if user_input:
    # Add human message
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    st.session_state.chat_display.append(("You", user_input))

    # Invoke Gemini model
    response = llm.invoke(st.session_state.chat_history)

    # Add AI response
    st.session_state.chat_history.append(AIMessage(content=response.content))
    st.session_state.chat_display.append(("AI", response.content))

# Display chat history
for sender, message in st.session_state.chat_display:
    if sender == "You":
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").write(message)
