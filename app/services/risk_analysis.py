print("risk_analysis.py LOADED")

import re

SCAM_KEYWORDS = [
    "urgent",
    "verify",
    "account",
    "suspended",
    "click",
    "login",
    "password",
    "bank",
    "otp",
]


def analyze_message(text: str) -> dict:
    print("analyze_message() CALLED")

    text_lower = text.lower()

    matched_keywords = [
        k for k in SCAM_KEYWORDS if k in text_lower
    ]

    has_link = bool(re.search(r"https?://|www\\.", text_lower))
    has_urgency = "urgent" in text_lower

    risk_score = 0
    risk_score += len(matched_keywords) * 2
    risk_score += 3 if has_link else 0
    risk_score += 2 if has_urgency else 0

    return {
        "risk_score": risk_score,
        "matched_keywords": matched_keywords,
    }
