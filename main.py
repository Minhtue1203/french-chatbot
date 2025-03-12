from fastapi import FastAPI
from pydantic import BaseModel
import openai
from dotenv import load_dotenv
import os
import prompt

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

app = FastAPI()


class TextRequest(BaseModel):
    text: str
    style: str = "standard"  # Par défaut, le style est neutre

@app.post("/correct")
async def correct_text(request: TextRequest):
    """Corrige le texte en fonction du style sélectionné."""
    messages = [
        {"role": "system", "content": prompt.get_system_message()},
        {"role": "user", "content": prompt.generate_prompt(request.text, request.style)}
    ]

    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )

    corrected_text = completion.choices[0].message.content

    return {
        "original_text": request.text,
        "corrected_text": corrected_text,
        "style": request.style
    }