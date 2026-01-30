# soulpage-genai-assignment2-rohit
End-to-end GenAI assignment showcasing a conversational AI bot with memory and external tools.

## 🚀 Deployment Notes

The conversational bot is designed to be easily deployable using **Streamlit Cloud**.

### Deployment Requirements
- Python 3.10+
- Streamlit
- Google Generative AI SDK
- Requests library

All dependencies are listed in `requirements.txt`.

### Environment Configuration
The application requires the following environment variables, which should be configured using **Streamlit Secrets** during deployment:

- `GOOGLE_API_KEY` – Gemini LLM access
- `SERPAPI_API_KEY` – Web search integration

No API keys are hard-coded in the source code.

### Memory Design
Due to changes in recent LangChain versions, `ConversationBufferMemory` is no longer available.
To maintain conversational context, the application uses **manual in-memory conversation storage**, where prior user–assistant interactions are persisted and injected into each prompt.
This achieves equivalent conversational continuity and meets the task requirements.

### Deployment Steps (Streamlit Cloud)
1. Push the repository to GitHub (public)
2. Create a new Streamlit app
3. Set the app entry point to: task2_conversational_bot/app.py
4. Add required API keys in Streamlit Secrets
5. Deploy the app

Once deployed, users can interact with the bot through a live chat interface.

---

### Sample Chat Log

You: who is ceo of OpenAI

Bot: Sam Altman is the CEO of OpenAI.

You: where sam Altman studied?

Bot: Sam Altman studied computer science at Stanford University.
