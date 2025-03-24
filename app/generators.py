import os
import openai
from dotenv import load_dotenv
import httpx
from openai import AsyncOpenAI



load_dotenv()
#создание клиента
client = AsyncOpenAI(api_key = os.getenv("AI_TOKEN"))


async def gpt4(question):
    response = await client.chat.completions.create( #создали запрос
        messages=[{"role": "system", "content": "You are a legal advisor for a citizen of Kazakhstan. "
                                                "Explain which articles of the Constitution "
                                                "are applicable in his situation towards the user and his aggressor."},
                  {"role": "user",
                   "content": str(question)}],
        model = "gpt-4o-mini",
        max_tokens = 350,
        frequency_penalty = 0.5,
    )
    return response
