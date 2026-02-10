import os

from fastapi import APIRouter, Form, Request, HTTPException
from twilio.request_validator import RequestValidator
from twilio.twiml.messaging_response import MessagingResponse

from app.services.risk_analysis import analyze_message
from app.services.risk_interpretation import interpret_risk

print("ENV =", os.getenv("ENV"))

router = APIRouter(prefix="/webhook")

IS_DEV = os.getenv("ENV", "dev") == "dev"


@router.post("/whatsapp")
async def whatsapp_webhook(
    request: Request,
    Body: str = Form(None),
    From: str = Form(None),
):
    response = MessagingResponse()

    # --- SECURITY (PROD ONLY) ---
    if not IS_DEV:
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        if not auth_token:
            raise RuntimeError("TWILIO_AUTH_TOKEN is not set")

        signature = request.headers.get("X-Twilio-Signature")
        if not signature:
            raise HTTPException(status_code=403, detail="Missing Twilio signature")

        form_data = await request.form()
        validator = RequestValidator(auth_token)

        if not validator.validate(str(request.url), form_data, signature):
            raise HTTPException(status_code=403, detail="Invalid Twilio signature")

    # --- BUSINESS LOGIC ---
    if not Body:
        response.message("Empty message received.")
        return str(response)

    analysis = analyze_message(Body)
    user_message = interpret_risk(analysis)

    response.message(user_message)
    return str(response)
