from flask import Flask, request, jsonify

from services.extractor import Extractor
from services.embedding_service import VertexEmbeddingService
from services.rag_service import RAGService
from services.grade_service import GradeService
from services.fine_tune_service import FineTuneService

app = Flask(__name__)

extractor = Extractor()
embedding_service = VertexEmbeddingService()
rag_service = RAGService()
grade_service = GradeService()
fine_tune_service = FineTuneService()

@app.route('/api/extract', methods=['POST'])
def extract():
    data = request.get_json(force=True)
    content = data.get('content', '')
    result = extractor.extract(content)
    return jsonify(result)

@app.route('/api/embeddings/generate', methods=['POST'])
def embeddings_generate():
    data = request.get_json(force=True)
    texts = data.get('texts', [])
    embeddings = embedding_service.generate_embeddings(texts)
    return jsonify({'embeddings': embeddings})

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json(force=True)
    prompt = data.get('prompt', '')
    response = rag_service.generate(prompt)
    return jsonify({'response': response})

@app.route('/api/grade', methods=['POST'])
def grade():
    data = request.get_json(force=True)
    submission = data.get('submission', '')
    result = grade_service.grade(submission)
    return jsonify(result)

@app.route('/api/fine-tune', methods=['POST'])
def fine_tune():
    data = request.get_json(force=True)
    params = data.get('params', {})
    job = fine_tune_service.fine_tune(params)
    return jsonify({'job': job})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
