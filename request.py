import requests
import json

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-type": "application/json",
    "Authorization": "Bearer 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"
}

data = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "user", "content": "что такое n8n"},
    ]
}

response = requests.post(url, headers=headers, json=data)

result = response.json()
print(result["choices"][0]["message"]["content"])