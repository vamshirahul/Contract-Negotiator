# services/clause_extractor.py
import json
from core.llm import call_llm
from core.prompts import SYSTEM_PROMPT, CLAUSE_EXTRACTION_PROMPT

def extract_clauses(contract_text: str):
    prompt = CLAUSE_EXTRACTION_PROMPT.format(contract_text=contract_text)
    response = call_llm(SYSTEM_PROMPT, prompt)
    return json.loads(response)
