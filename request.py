import requests
import json

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-type": "application/json",
    "Authorization": "Bearer API Key"
}

data = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "user", "content": "что такое n8n и для чего она нужна"},
    ]
}

response = requests.post(url, headers=headers, json=data)

result = response.json()
print(result["choices"][0]["message"]["content"])