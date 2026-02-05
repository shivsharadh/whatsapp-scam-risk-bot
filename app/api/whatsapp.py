from fastapi import APIRouter, Form

router = APIRouter(prefix="/webhook")


@router.post("/whatsapp")
async def whatsapp_webhook(
    Body: str = Form(...),
    From: str = Form(None),
):
    """
    Entry point for WhatsApp messages via Twilio.

    At this stage, this endpoint only confirms receipt of the message.
    """
    return {
        "status": "received",
        "from": From,
        "body": Body,
    }
