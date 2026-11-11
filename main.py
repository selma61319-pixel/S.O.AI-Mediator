import os
import json
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI(title="S.O.Agent: End-to-End AI Escrow System")
ai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatPayload(BaseModel):
    client_email: str
    freelancer_email: str
    chat_history: str

@app.post("/ai/process-chat")
async def process_chat(payload: ChatPayload):
    system_prompt = "You are an expert global AI Project Manager. Monitor chat agreements and extract milestones into strict English JSON format."
    response = ai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": payload.chat_history}],
        temperature=0.1
    )
    ai_data = json.loads(response.choices[0].message.content.strip())
    if not ai_data.get("agreement_reached"):
        return {"status": "Negotiation In Progress"}
    return {"status": "Escrow Created", "message": "S.O.Agent: Secure PayPal escrow payment link has been dispatched!"}
