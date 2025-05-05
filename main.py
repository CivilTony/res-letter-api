from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# CORS to allow GPT to talk to your API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LetterInput(BaseModel):
    prompt: str

@app.post("/generate_letter_json")
async def generate_letter_json(data: LetterInput):
    # ⚠️ Replace this mock JSON with real logic or LLM inference
    return {
        "letter_data": {
            "report_date": "May 4th, 2025",
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
            "body": "We have completed the requested inspection...",
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
