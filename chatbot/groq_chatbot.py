import requests
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Set via Streamlit Secrets or Env Var

def groq_chatbot(prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "messages": [{"role": "user", "content": prompt}],
        "model": "llama3-8b-8192"
    }
    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]
