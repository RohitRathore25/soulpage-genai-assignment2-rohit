import os
import requests
import google.generativeai as genai

SERPAPI_KEY = os.getenv("SERP_API")
GEMINI_API_KEY = os.getenv('GOOGLE_API_KEY4')

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash-lite',
                              generation_config={'temperature':0.2})

def web_search(query: str) -> str:
    """
    Fetch search results using SerpAPI (Google Search)
    """
    if not SERPAPI_KEY:
        return "SERPAPI_KEY not set."

    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "engine": "google",
        "api_key": SERPAPI_KEY,
        "num": 3
    }

    response = requests.get(url, params=params, timeout=10)
    results = response.json().get("organic_results", [])

    snippets = []
    for r in results[:3]:
        snippet = r.get("snippet")
        if snippet:
            snippets.append(snippet)

    return "\n".join(snippets) if snippets else "No search results found."
