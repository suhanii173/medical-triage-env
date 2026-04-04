from pydantic import BaseModel
from typing import List

class Observation(BaseModel):
    patient_id: int
    age: int
    symptoms: List[str]
    heart_rate: int
    bp: str

class Action(BaseModel):
    triage_level: str

class Reward(BaseModel):
    score: float