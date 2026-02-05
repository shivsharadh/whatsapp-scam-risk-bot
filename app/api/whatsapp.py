from fastapi import APIRouter, Form, Request, HTTPException
from twilio.twiml.messaging_response import MessagingResponse
from twilio.request_validator import RequestValidator
import os

router = APIRouter(prefix="/webhook")


@router.post("/whatsapp")
async def whatsapp_webhook(
    request: Request,
    Body: str = Form(None),
    From: str = Form(None),
):
    """
    Entry point for WhatsApp messages via Twilio.
    Security: validates Twilio request signature.
    """

    # --- Signature validation ---
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    if not auth_token:
        raise RuntimeError("TWILIO_AUTH_TOKEN is not set")

    signature = request.headers.get("X-Twilio-Signature")
    if not signature:
        raise HTTPException(status_code=403, detail="Missing Twilio signature")

    validator = RequestValidator(auth_token)

    url = str(request.url)
    form_data = await request.form()

    if not validator.validate(url, form_data, signature):
        raise HTTPException(status_code=403, detail="Invalid Twilio signature")

    # --- Business stub ---
    response = MessagingResponse()

    if not Body:
        response.message("Empty message received.")
        return str(response)

    response.message("Message received. Processing risk assessment.")
    return str(response)
