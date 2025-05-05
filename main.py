from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

app = FastAPI(title="RES Letter JSON Generator", version="1.0.0")

# Allow GPT to reach this endpoint
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Can restrict to *.openai.com if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------
# 📬 Input Model
# ----------------------

class LetterInput(BaseModel):
    prompt: str

# ----------------------
# 📤 Output Model (Optional for stricter validation)
# ----------------------

class AppendixSection(BaseModel):
    title: str
    content: str

class LetterResponse(BaseModel):
    letter_data: dict

# ----------------------
# 📅 Helper to generate today's date in pretty format
# ----------------------


def get_pretty_date():
    today = date.today()
    day = today.day
    suffix = "th" if 11 <= day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
    return today.strftime(f"%B {day}{suffix}, %Y")

# ----------------------
# 🔧 Main Endpoint
# ----------------------
@app.post("/generate_letter_json", response_model=LetterResponse)
async def generate_letter_json(data: LetterInput):
    prompt_text = data.prompt.strip()

    # TODO: Replace this with prompt-driven logic or GPT response parsing
    return {
        "letter_data": {
            "report_date": get_pretty_date(),
            "recipient_name": "City of Lakewood",
            "subject": "Structural Observation",
            "project_address": "123 Main Street, Lakewood, CO",
            "engineer_name": "A. Ruffini",
            "engineer_title": "P.E., Principal Engineer",
            "engineer_credentials": "P.E., S.E.",
            "engineer_phone": "(720) 555-1234",
            "engineer_email": "anthony@res-civil.com",
            "engineer_licenses": "CO 001234, FL 56789",
            "salutation": "Building Official",
            "body": "We have completed the requested inspection and offer our findings.",
            "executive_summary": "",
            "scope_of_work": "",
            "site_visit_summary": "",
            "observed_conditions": "",
            "deficiencies": "",
            "code_review": "",
            "load_path_review": "",
            "foundation_review": "",
            "include_appendix": True,
            "appendix_sections": [],
            "photo_page": [],
            "include_digital_stamp": True
        }
    }
