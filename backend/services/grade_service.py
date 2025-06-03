"""Service to evaluate grant drafts using LLM prompts."""

from typing import Any, Dict


class GradeService:
    """Grade submissions with prompt-based evaluation."""

    def grade(self, submission: str) -> Dict[str, Any]:
        """Return a score and feedback for the given submission."""
        # Placeholder logic; replace with actual prompt-based grading
        score = len(submission) % 100
        return {"score": score, "feedback": "Generated feedback"}
