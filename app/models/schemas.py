from pydantic import BaseModel
from typing import List


class GenerateResponse(BaseModel):
    objective: str
    optimized_prompt: str
    improvements: List[str]


class EvaluateResponse(BaseModel):
    score: int
    strengths: list[str]
    weaknesses: list[str]
    suggestions: list[str]

    # New Feature (Backward Compatible)
    recommended_lines: list[str] = []


class PipelineResponse(BaseModel):
    generation: GenerateResponse
    evaluation: EvaluateResponse


# ==========================
# NEW: Redesign Models
# ==========================

class PromptVersion(BaseModel):
    title: str
    score: float
    prompt: str


class RedesignResponse(BaseModel):
    professional: PromptVersion
    expert: PromptVersion