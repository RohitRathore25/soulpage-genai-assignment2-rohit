import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import google.generativeai as genai
from tools import web_search
from memory import get_memory


SERPAPI_KEY = os.getenv("SERP_API")
GEMINI_API_KEY = os.getenv('GOOGLE_API_KEY4')


# Initialize Gemini LLM
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash-lite',
                              generation_config={'temperature':0.2})



def run_bot(user_question: str, memory):
    """
    Runs the conversational knowledge bot
    """

    # Fetch external knowledge
    context = web_search(user_question)

    # Prompt with memory + context
    prompt = ChatPromptTemplate.from_template("""
    You are a factual and helpful assistant.

    External Knowledge:
    {context}

    Conversation History:
    {chat_history}

    User Question:
    {question}

    Answer clearly and concisely.
    """)
    
    
    messages = prompt.format_messages(
        context=context,
        chat_history=memory.chat_memory.messages,
        question=user_question
    )


    response = model.predict(messages[0].content)

    # Save conversation to memory
    memory.save_context(
        {"input": user_question},
        {"output": response}
    )

    return response
