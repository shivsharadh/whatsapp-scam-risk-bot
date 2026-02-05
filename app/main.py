from fastapi import FastAPI

from app.api.whatsapp import router as whatsapp_router

app = FastAPI(title="WhatsApp Scam Risk Bot")

app.include_router(whatsapp_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
