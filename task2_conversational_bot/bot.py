import os
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import web_search
import google.generativeai as genai



SERPAPI_KEY = os.getenv("SERP_API")
GEMINI_API_KEY = os.getenv('GOOGLE_API_KEY4')


# Initialize Gemini LLM
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash-lite',
                              generation_config={'temperature':0.2})

# Manual conversation memory
conversation_history = []

def run_bot(user_input: str) -> str:
    global conversation_history

    # Convert history into text
    history_text = ""
    for user, bot in conversation_history:
        history_text += f"User: {user}\nBot: {bot}\n"

    # External search context
    context = web_search(user_input)
    
    
    prompt = f"""
<Role>
You are a conversational knowledge assistant.

<Context>
Conversation History:
{history_text}

External Knowledge:
{context}

<User Question>
{user_input}

<Instructions>
- Answer factually and clearly
- Use prior conversation context if relevant
- Keep responses concise
"""

    response = model.generate_content(prompt).text

    # Save to memory
    conversation_history.append((user_input, response))

    return response

