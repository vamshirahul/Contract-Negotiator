# core/schemas.py
from pydantic import BaseModel
from typing import List, Optional

class Clause(BaseModel):
    clause_id: str
    heading: str
    text: str
    category: str

class RiskItem(BaseModel):
    risk_id: str
    category: str
    severity: str
    why_it_matters: str
    recommended_position: str
    fallback_position: Optional[str]
    clause_id: str
