import requests
import os
import streamlit as st

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

def groq_chatbot(prompt):
    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "model": "meta-llama/llama-4-scout-17b-16e-instruct"
    }

    # ✅ Add Authorization header
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        json=payload,
        headers=headers
    )

    # Logging for debugging
    print("Status code:", response.status_code)
    print("Response JSON:", response.json())

    data = response.json()
    if "choices" in data:
        return data["choices"][0]["message"]["content"]
    else:
        return f"API error: {data.get('error', 'Unknown error')}"
