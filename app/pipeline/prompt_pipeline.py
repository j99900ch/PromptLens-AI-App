from app.agents.generate import GenerateAgent
from app.agents.evaluate import EvaluateAgent
from app.agents.redesign import RedesignAgent


class PromptPipeline:
    """
    Main AI Pipeline.

    Order:
        1. Generate optimized prompt
        2. Evaluate optimized prompt
        3. Generate two redesigned prompt versions
    """

    def __init__(self):
        self.generator = GenerateAgent()
        self.evaluator = EvaluateAgent()
        self.redesigner = RedesignAgent()

    def run(self, user_prompt: str):

        # -------------------------
        # Generate
        # -------------------------

        generation = self.generator.run(user_prompt)

        # -------------------------
        # Evaluate
        # -------------------------

        evaluation = self.evaluator.run(
            generation.optimized_prompt
        )

        # -------------------------
        # Redesign
        # -------------------------

        redesign = self.redesigner.run(
            generation.optimized_prompt
        )

        # -------------------------
        # Return everything
        # -------------------------

        return {
            "generation": generation,
            "evaluation": evaluation,
            "redesign": redesign,
        }