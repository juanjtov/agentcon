from flask import Flask, jsonify, render_template, request
import numpy as np
from sentence_transformers import SentenceTransformer
import os

import helpers

# Get the directory where this file is located
TASK_DIR = os.path.dirname(os.path.abspath(__file__))
# Get the project root (two levels up from task_11.py)
PROJECT_ROOT = os.path.dirname(os.path.dirname(TASK_DIR))

app = Flask(__name__, template_folder=os.path.join(TASK_DIR, "templates"))

# Use absolute paths based on project root
CHUNK_PATH = os.path.join(PROJECT_ROOT, "outputs/task_8_chunks.json")
EMBEDDING_PATH = os.path.join(PROJECT_ROOT, "outputs/task_8_embeddings.pkl")
OUTPUT_PATH = os.path.join(PROJECT_ROOT, "outputs/task_11.json")

# Global variables for caching
_model = None
_chunks = None
_embeddings = None


def get_model():
    """Lazy load the SentenceTransformer model."""
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


def get_chunks_and_embeddings():
    """Lazy load chunks and embeddings."""
    global _chunks, _embeddings
    if _chunks is None:
        _chunks = helpers.load_json(CHUNK_PATH)
    if _embeddings is None:
        _embeddings = helpers.load_pickle(EMBEDDING_PATH)
    return _chunks, _embeddings


def retrieve_chunks(query, top_k=5):
    """
    Retrieve the most similar chunks to the query.
    Returns both nearest and furthest chunks with similarity scores.
    """
    model = get_model()
    chunks, embeddings = get_chunks_and_embeddings()
    
    # Embed the query
    query_embedding = model.encode([query])[0]
    
    # Compute cosine similarity
    query_norm = query_embedding / np.linalg.norm(query_embedding)
    chunk_norms = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
    similarities = np.dot(chunk_norms, query_norm)
    
    # Get sorted indices
    sorted_indices = np.argsort(similarities)[::-1]
    
    # Top k nearest chunks
    nearest_indices = sorted_indices[:top_k]
    # Top k furthest chunks  
    furthest_indices = sorted_indices[-top_k:][::-1]
    
    nearest_chunks = []
    for idx in nearest_indices:
        chunk = chunks[idx]
        nearest_chunks.append({
            "chunk_id": f"chunk_{idx}",
            "source_file": chunk["source_file"],
            "chunk_index": chunk["chunk_index"],
            "text": chunk["text"],
            "similarity_score": float(similarities[idx]),
            "type": "similar"
        })
    
    furthest_chunks = []
    for idx in furthest_indices:
        chunk = chunks[idx]
        furthest_chunks.append({
            "chunk_id": f"chunk_{idx}",
            "source_file": chunk["source_file"],
            "chunk_index": chunk["chunk_index"],
            "text": chunk["text"],
            "similarity_score": float(similarities[idx]),
            "type": "different"
        })
    
    return nearest_chunks, furthest_chunks, similarities.tolist()


def generate_insights(query, nearest_chunks, furthest_chunks):
    """
    Generate insights with citations using the LLM.
    """
    # Build context from all chunks
    context_chunks = nearest_chunks + furthest_chunks
    context_text = ""
    for i, chunk in enumerate(context_chunks, 1):
        context_text += f"\n--- Chunk {i} (Source: {chunk['source_file']}, Type: {chunk['type']}, Score: {chunk['similarity_score']:.4f}) ---\n"
        context_text += chunk["text"]
        context_text += "\n"
    
    # Create LLM instance
    llm = helpers.LlmModel()
    
    # Generate improved answer with citations
    generation_prompt = f"""You are an expert at synthesizing information from multiple sources to answer user queries.

USER QUERY: {query}

RETRIEVED CONTEXT:
{context_text}

Instructions:
- Analyze all retrieved chunks (both similar and different) to extract relevant insights
- Generate a comprehensive answer to the user query
- For each insight, provide:
  1. The insight itself
  2. A justification explaining why this insight is relevant
  3. A citation with the source file
- Focus on actionable, specific advice
- Return your response as a JSON object with the following structure:

{{
    "summary": "A brief overall summary answering the user's question",
    "insights": [
        {{
            "insight": "The specific insight or recommendation",
            "justification": "Why this insight is relevant and helpful",
            "citation": "The source file where this information was found"
        }}
    ]
}}

Return ONLY valid JSON, no other text.
"""
    
    response = llm.prompt_llm(generation_prompt, get_structured_output="json")
    return response


@app.route("/")
def index():
    """Serve the main search interface."""
    return render_template("task_11_index.html")


@app.route("/query", methods=["POST"])
def query_endpoint():
    """Handle search queries and return insights with citations."""
    try:
        data = request.get_json()
        if not data or "query" not in data:
            return jsonify({"error": "No query provided"}), 400
        
        query = data["query"].strip()
        if not query:
            return jsonify({"error": "Query cannot be empty"}), 400
        
        # Retrieve relevant chunks
        nearest_chunks, furthest_chunks, all_similarities = retrieve_chunks(query, top_k=3)
        
        # Generate insights with LLM
        insights_response = generate_insights(query, nearest_chunks, furthest_chunks)
        
        # Prepare response
        response_data = {
            "query": query,
            "retrieved_chunks": nearest_chunks + furthest_chunks,
            "summary": insights_response.get("summary", ""),
            "insights": insights_response.get("insights", []),
            "similarity_distribution": {
                "labels": [f"Chunk {i}" for i in range(len(all_similarities))],
                "scores": all_similarities[:20]  # Limit to first 20 for visualization
            }
        }
        
        # Save to output file
        helpers.save_json(response_data, OUTPUT_PATH)
        
        return jsonify(response_data)
    
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@app.route("/health")
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "service": "Deep Research RAG"})


def task_11():
    """
    Goal:
        Launch the Flask app which looks like Google with a nicer background where the user types a user query and outputs the insights and citations from the 3 files
    Instructions for task 11:
        - Create a Flask app with a query endpoint that returns insights and citations based on a user query.
        - Use the RAG mechanisms from tasks 8, 9, 10
        - You can copy paste the relevant code from those tasks into small helper functions here
        - Save the outputs in task_11.json
    """
    print("\n" + "="*60)
    print("🚀 Starting Deep Research RAG Flask App")
    print("="*60)
    print("\n📍 Server running at: http://127.0.0.1:5000")
    print("📊 Health check: http://127.0.0.1:5000/health")
    print("\n💡 Press Ctrl+C to stop the server\n")
    
    app.run(debug=True, host="0.0.0.0", port=5000)


if __name__ == "__main__":
    task_11()
