from fastapi import APIRouter, Form
from twilio.twiml.messaging_response import MessagingResponse

router = APIRouter(prefix="/webhook")


@router.post("/whatsapp")
async def whatsapp_webhook(
    Body: str = Form(None),
    From: str = Form(None),
):
    """
    Entry point for WhatsApp messages via Twilio.
    At this stage, the endpoint only acknowledges receipt.
    """

    response = MessagingResponse()

    if not Body:
        response.message("Empty message received.")
        return str(response)

    response.message("Message received. Processing risk assessment.")
    return str(response)
