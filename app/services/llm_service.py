import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_response(prompt: str):

    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json()["response"]
    else:
        return "Error generating response."

print(generate_response("Hello mistral"))