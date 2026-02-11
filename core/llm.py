# core/llm.py
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def call_llm(system_prompt: str, user_prompt: str, temperature=0.2):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=temperature
    )
    return response.choices[0].message.content
