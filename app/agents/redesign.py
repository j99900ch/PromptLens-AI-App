import json

from app.services.llm_service import LLMService


class RedesignAgent:
    """
    Generates two improved prompt versions.

    Version 1:
        Professional

    Version 2:
        Expert

    Returns structured JSON.
    """

    def __init__(self):
        self.llm = LLMService()

    def run(self, prompt: str):

        redesign_prompt = f"""
You are an expert Prompt Engineer.

The user wrote:

{prompt}

Generate TWO redesigned versions.

Version 1:
Professional

Version 2:
Expert

Both versions should automatically include:

- missing context
- target audience
- role
- tone
- output format
- constraints
- best practices

Return ONLY valid JSON.

{{
    "professional": {{
        "title":"Professional",
        "score":9.2,
        "prompt":"..."
    }},
    "expert": {{
        "title":"Expert",
        "score":9.8,
        "prompt":"..."
    }}
}}
"""

        response = self.llm.generate(redesign_prompt)

        response = (
            response.replace("```json", "")
                    .replace("```", "")
                    .strip()
        )

        return json.loads(response)