import os
from dotenv import load_dotenv

load_dotenv()

CHAT_COMPLETION_API_BASE_URL = os.getenv('CHAT_COMPLETION_API_BASE_URL')
API_KEY=os.getenv('API_KEY')
MODEL_NAME='gpt-3.5-turbo'
RANDOMIZE =0.7