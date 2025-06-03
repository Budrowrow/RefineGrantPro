"""Retrieval-Augmented Generation service using Vertex LLM."""

from typing import Any

from google.cloud import aiplatform


class RAGService:
    """Simple wrapper around a Vertex AI generative model."""

    def __init__(self, model_name: str = "chat-bison@001"):
        aiplatform.init()
        self.model = aiplatform.GenerativeModel(model_name)

    def generate(self, prompt: str, **kwargs: Any) -> str:
        """Generate a response using the underlying model."""
        if not prompt:
            return ""
        response = self.model.predict(prompt, **kwargs)
        return response.text
