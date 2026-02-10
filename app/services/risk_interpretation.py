print("risk_interpretation.py LOADED")


def interpret_risk(analysis: dict) -> str:
    print("interpret_risk() CALLED")

    score = analysis.get("risk_score", 0)
    keywords = analysis.get("matched_keywords", [])

    if score >= 7:
        return (
            "⚠️ High scam risk detected.\n"
            "This message shows multiple red flags such as urgency or suspicious links.\n"
            "Do NOT click links or share personal information."
        )

    if score >= 4:
        return (
            "⚠️ Medium scam risk.\n"
            "Be cautious. Verify the sender before taking any action."
        )

    return (
        "✅ Low scam risk.\n"
        "No obvious scam indicators detected, but always stay alert."
    )
