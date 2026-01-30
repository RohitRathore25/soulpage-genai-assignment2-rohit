import os
import streamlit as st
from bot import run_bot
from memory import get_memory
import google.generativeai as genai


SERPAPI_KEY = os.getenv("SERP_API")
GEMINI_API_KEY = os.getenv('GOOGLE_API_KEY4')

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash-lite',
                              generation_config={'temperature':0.2})



st.set_page_config(page_title="Conversational Knowledge Bot")

st.title("Conversational Knowledge Bot")
st.write("Gemini + SerpAPI + Conversation Memory")

# Initialize memory once
if "memory" not in st.session_state:
    st.session_state.memory = get_memory()

# Store chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("Ask a question")

if st.button("Send") and user_input.strip():
    response = run_bot(user_input, st.session_state.memory)

    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("Bot", response))

# Display chat
for speaker, message in st.session_state.messages:
    st.markdown(f"**{speaker}:** {message}")
