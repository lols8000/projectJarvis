import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPEN_API_KEY")

def informacao(texto):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Me fale sobre: {texto}",
        temperature=0.7,
        max_tokens=2048,
        n=1,
        stop=None
    )
    return response['choices'][0]['text'].strip()
