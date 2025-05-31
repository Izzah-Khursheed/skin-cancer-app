import requests
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY") 

def groq_chatbot(user_input):
    payload = {
        "messages": [{"role": "user", "content": user_input}],
        "model": "meta-llama/llama-4-scout-17b-16e-instruct"
    }
    response = requests.post("https://api.groq.com/openai/v1/chat/completions", json=payload)
    
    print("Status code:", response.status_code)  # or use logging
    print("Response JSON:", response.json())     # or use logging
    
    # Check for 'choices' key before accessing
    data = response.json()
    if "choices" in data:
        return data["choices"][0]["message"]["content"]
    else:
        # Handle error gracefully, return error message or raise informative error
        return f"API error: {data.get('error', 'Unknown error')}"


# import requests
# import os

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Set via Streamlit Secrets or Env Var

# def groq_chatbot(prompt):
#     headers = {
#         "Authorization": f"Bearer {GROQ_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     data = {
#         "messages": [{"role": "user", "content": prompt}],
#         "model": "meta-llama/llama-4-scout-17b-16e-instruct"
#     }
#     response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
#     return response.json()["choices"][0]["message"]["content"]
