# services/risk_analyzer.py
import json
from core.llm import call_llm
from core.prompts import SYSTEM_PROMPT, RISK_ANALYSIS_PROMPT

def analyze_risks(clauses: list):
    prompt = RISK_ANALYSIS_PROMPT.format(
        clauses_json=json.dumps(clauses, indent=2)
    )
    response = call_llm(SYSTEM_PROMPT, prompt)
    return json.loads(response)
