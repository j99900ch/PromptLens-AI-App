import json

from app.services.llm_service import LLMService
from app.models.schemas import EvaluateResponse


class EvaluateAgent:
    """
    Evaluates an optimized prompt and returns structured feedback.
    """

    def __init__(self):
        self.llm = LLMService()

    def run(self, optimized_prompt: str) -> EvaluateResponse:

        prompt = f"""
You are an expert AI Prompt Engineer and Prompt Reviewer.

Evaluate the following prompt carefully.

Return ONLY valid JSON.

Format:

{{
    "score": 0,
    "strengths": [
        "...",
        "...",
        "..."
    ],
    "weaknesses": [
        "...",
        "...",
        "..."
    ],
    "suggestions": [
        "...",
        "...",
        "..."
    ],
    "recommended_lines": [
        "...",
        "...",
        "...",
        "...",
        "..."
    ]
}}

Rules:

1. Score the prompt from 0-10.

2. Strengths should explain what is already good.

3. Weaknesses should explain what is missing.

4. Suggestions should explain HOW to improve the prompt.

5. recommended_lines must contain ready-to-copy lines that the user can directly add to the prompt.

6. The recommended_lines MUST be specific to THIS prompt.
Do NOT generate generic advice.

Example:

If the prompt is about a Resume:

[
"Target Role: Python Backend Developer",
"Optimize for ATS compatibility.",
"Include measurable achievements.",
"Use a professional tone.",
"Limit the response to one page."
]

If the prompt is about LinkedIn:

[
"Audience: Recruiters",
"Tone: Professional and confident.",
"Highlight measurable achievements.",
"Keep within 250 words.",
"Include relevant industry keywords."
]

Prompt:

{optimized_prompt}
"""

        response = self.llm.generate(prompt)

        response = (
            response.replace("```json", "")
                    .replace("```", "")
                    .strip()
        )

        data = json.loads(response)

        return EvaluateResponse(**data)