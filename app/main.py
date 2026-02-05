from fastapi import FastAPI

app = FastAPI(title="WhatsApp Scam Risk Bot")


@app.get("/health")
def health_check():
    return {"status": "ok"}