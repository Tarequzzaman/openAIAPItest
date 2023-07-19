import os
import json
import requests
from config import (
    API_KEY,
    CHAT_COMPLETION_API_BASE_URL,
    MODEL_NAME, 
    RANDOMIZE 
    )

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + API_KEY
}

json_data = {
    'model': MODEL_NAME,
    'messages': [
        {
            'role': 'user',
            'content': 'Say this is a test!',
        },
    ],
    'temperature': RANDOMIZE, #how much randomize the model
}

response = requests.post(CHAT_COMPLETION_API_BASE_URL, headers=headers, json=json_data)
print(response.status_code)

print(response.json())