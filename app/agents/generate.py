import json

from app.services.llm_service import LLMService
from app.models.schemas import GenerateResponse


class GenerateAgent:
    """
    Generates an optimized prompt and returns structured data.
    """

    def __init__(self):
        self.llm = LLMService()

    def run(self, user_prompt: str) -> GenerateResponse:

        prompt = f"""
You are PromptLens AI.

Return ONLY valid JSON.

Format:

{{
    "objective":"...",
    "optimized_prompt":"...",
    "improvements":[
        "...",
        "...",
        "..."
    ]
}}

User Prompt:

{user_prompt}
"""

        response = self.llm.generate(prompt)

        # Remove markdown code fences if present
        response = response.replace("```json", "").replace("```", "").strip()

        data = json.loads(response)

        return GenerateResponse(**data)