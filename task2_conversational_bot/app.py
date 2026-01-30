import streamlit as st
from bot import run_bot
import google.generativeai as genai
import os



SERPAPI_KEY = os.getenv("SERP_API")
GEMINI_API_KEY = os.getenv('GOOGLE_API_KEY4')


# Initialize Gemini LLM
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash-lite',
                              generation_config={'temperature':0.2})


st.set_page_config(page_title="Conversational Knowledge Bot")
st.title("💬 Conversational Knowledge Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Ask a question")

if st.button("Send") and user_input:
    response = run_bot(user_input)

    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("Bot", response))

# Display chat history
for speaker, message in st.session_state.messages:
    st.markdown(f"**{speaker}:** {message}")

