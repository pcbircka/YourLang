from fastapi import FastAPI

app = FastAPI()

@app.get("/transcribe")
def transcribe():
    return {"status": "ok", "message": "transcribe endpoint"}

@app.get("/extract_keywords")
def extract_keywords():
    return {"status": "ok"}

@app.get("/translate")
def translate():
    return {"status": "ok"}

@app.get("/generate_vocabulary")
def generate_vocab():
    return {"status": "ok"}

