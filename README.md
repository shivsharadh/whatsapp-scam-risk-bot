# WhatsApp Scam Risk Bot

A WhatsApp bot that assesses the **risk of scam and phishing messages** using
rule-based NLP signals and machine learning.

This project is intentionally designed as a **risk assessment system**, not a
binary scam detector.

---

## Why This Project Exists

Scam and phishing messages rely more on **patterns and social engineering**
than on factual correctness. Instead of trying to label messages as “scam” or
“safe”, this project focuses on:

- Identifying common scam signals
- Assigning a risk score
- Explaining *why* a message looks risky
- Helping users make better decisions under uncertainty

The goal is **trustworthy guidance**, not perfect detection.

---

## What This Project Is (and Is Not)

### This project **is**:
- A FastAPI backend exposing a WhatsApp webhook
- A hybrid system using:
  - Rule-based NLP signals (high precision)
  - ML-based NLP scoring (TF-IDF + classical models)
- A risk scorer that produces **probabilistic output**
- A system designed to be explainable and extensible

### This project **is not**:
- A fact-checking or fake news verification system
- A fully autonomous scam classifier
- A production-ready security product
- A transformer or LLM-based solution (by design)

---

## High-Level Architecture

WhatsApp User
↓
Twilio WhatsApp Webhook
↓
FastAPI Backend
├─ Rule-based NLP analysis
├─ ML-based NLP scoring
├─ Risk aggregation
├─ Human-readable explanation
↓
Risk assessment response


---

## Tech Stack

- **Backend**: Python, FastAPI
- **AI / ML**: NLP (rule-based + ML scoring)
- **Database**: MongoDB (for message logs, assessments, and feedback)
- **Integration**: Twilio API (WhatsApp)

---

## Project Philosophy

A few design principles guide this codebase:

- **Uncertainty is explicit**  
  The system never claims certainty where none exists.

- **Explainability over complexity**  
  Simpler models with clear reasoning are preferred over opaque accuracy gains.

- **Human trust over model confidence**  
  Output language is designed to advise, not alarm.

- **Incremental extensibility**  
  ML components are replaceable without rewriting the system.

---

## Current Status

- [x] FastAPI application skeleton
- [x] Health check endpoint
- [x] Dependency management
- [ ] WhatsApp webhook integration
- [ ] Rule-based NLP signal extraction
- [ ] ML-based NLP scoring
- [ ] MongoDB persistence
- [ ] User feedback loop

The project is being built **incrementally**, with each layer added only after
the previous one is stable and testable.

---

## Running Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
Verify:

GET http://127.0.0.1:8000/health
Disclaimer
This project provides risk assessment, not guarantees.
It should not be used as the sole basis for security decisions.

License
MIT


---

## 3️⃣ Stop and Review (Important)

Before committing, quickly sanity-check:
- No hype
- No fake accuracy claims
- No buzzwords
- Clear limitations
- Honest scope

This README passes a **senior engineer smell test**.

---

## 4️⃣ Commit (One Clean Commit)

Stage `README.md`

**Commit message (exactly):**
```text
docs: add developer-focused project overview