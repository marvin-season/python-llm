import requests
import json

country = "China"

schema = {
    "city": {
        "type": "string",
        "description": "Name of the city",
    },
    "latitude": {
        "type": "float",
        "description": "Decimal latitude of the city",
    },
    "longitude": {
        "type": "float",
        "description": "Decimal longitude of the city",
    }
}

payload = {
    "model": "llama3.1",
    "messages": [
        {
            "role": "system",
            "content": f"You are a helpful AI assistant. The user will enter a country name and the assistant will return the decimal latitude and decimal longitude of the capital of the country. Output in JSON, using the schema defined here: {schema}"
        },
        {
            "role": "user",
            "content": f"{country}"
        }
    ],
}

response = requests.post("http://localhost:11434/api/chat", json=payload)

for message in response.iter_lines():
    jsonstr = json.loads(message)
    print(jsonstr['message']['content'], end=' ')
