
from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
import stt, tts, chatbot, auth, config, utils
import os

app = FastAPI()

API_KEY_HEADER = APIKeyHeader(name="X-API-Key")

async def get_api_key(api_key_header: str = Depends(API_KEY_HEADER)):
    if api_key_header in config.API_KEYS:
        return api_key_header
    else:
        raise HTTPException(status_code=401, detail="Invalid API Key")

class ChatRequest(BaseModel):
    text: str

@app.post("/chat/")
async def chat(request: ChatRequest, api_key: str = Depends(get_api_key)):
    response = chatbot.generate_response(request.text)
    return {"response": response}

@app.post("/stt/")
async def speech_to_text(audio: UploadFile = File(...), api_key: str = Depends(get_api_key)):
    temp_file = "temp_audio.wav"
    with open(temp_file, "wb") as buffer:
        buffer.write(await audio.read())
    text = stt.transcribe_audio(temp_file)
    os.remove(temp_file)
    return {"text": text}

@app.post("/tts/")
async def text_to_speech(request: ChatRequest, api_key: str = Depends(get_api_key)):
    audio_file = tts.generate_speech(request.text)
    return {"audio_file": audio_file}
