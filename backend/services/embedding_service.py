"""Service for generating text embeddings using Vertex AI."""

from typing import List

from google.cloud import aiplatform


class VertexEmbeddingService:
    """Wrapper around Vertex AI's text embedding models."""

    def __init__(self, model_name: str = "textembedding-gecko@001"):
        self.model_name = model_name
        aiplatform.init()
        self.model = aiplatform.TextEmbeddingModel.from_pretrained(model_name)

    def generate_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for a list of texts."""
        if not texts:
            return []
        embeddings = self.model.get_embeddings(texts)
        return [emb.embedding for emb in embeddings]
