from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/ask")
async def ask_ai(data: dict):
    instrucciones = """Eres 'PRO-LUB', experto en Tribología y Lubricación de Molub Academy. 
    Tu tono es técnico y eficiente. Responde dudas sobre los 8 módulos del curso. 
    Si te preguntan algo fuera de tema, di que solo das soporte técnico de Molub."""
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": instrucciones},
            {"role": "user", "content": data["message"]}
        ]
    )
    return {"answer": response.choices[0].message.content}
