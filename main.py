from fastapi import FastAPI
from pydantic import BaseModel
import spacy

app = FastAPI()
nlp = spacy.load("en_core_web_sm")

class TextRequest(BaseModel):
    text: str

@app.post("/tokenize/")
def tokenize_text(req: TextRequest):
    doc = nlp(req.text)
    tokens = [token.text for token in doc]
    return {"tokens": tokens}
