from dotenv import load_dotenv
from groq import Groq
import os 

load_dotenv()

api_key = os.getenv("groq_api_key")
if api_key is None:
    raise RuntimeError("there is no api key in .env")

client = Groq(api_key=api_key)
def get_chat(message : list):

    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = message

    )
    return response.choices[0].message.content