import helpers
import numpy as np
from sentence_transformers import SentenceTransformer


def task_9():
    """
    Goal:
        Retrieve the 3 closest and 3 furthest chunks for a query and log their scores.
    Instructions:
        - Load the user query from outputs/task_4_groundtruth.json
        - Load the chunk metadata and embeddings from Task 8 outputs
        - Embed the query, score every chunk, and print the top 3 closest chunks
        - Save the query, its nearest chunks, and the most different chunks (with metadata) to outputs/task_9_retrieval_results.json
    """

    # Load the user query from task 4 groundtruth
    groundtruth = helpers.load_json("outputs/task_4_groundtruth.json")
    user_query = groundtruth["user_query"]
    print(f"User query: {user_query}")

    # Load chunk metadata and embeddings from Task 8
    chunks = helpers.load_json("outputs/task_8_chunks.json")
    embeddings = helpers.load_pickle("outputs/task_8_embeddings.pkl")
    print(f"Loaded {len(chunks)} chunks with embeddings shape: {embeddings.shape}")

    # Embed the query using the same model as Task 8
    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_embedding = model.encode([user_query])[0]

    # Compute cosine similarity between query and all chunks
    # Normalize embeddings for cosine similarity
    query_norm = query_embedding / np.linalg.norm(query_embedding)
    chunk_norms = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
    
    # Cosine similarity = dot product of normalized vectors
    similarities = np.dot(chunk_norms, query_norm)

    # Get indices sorted by similarity (descending for closest, ascending for furthest)
    sorted_indices = np.argsort(similarities)[::-1]
    
    # Top 3 closest chunks
    top_3_indices = sorted_indices[:3]
    # Top 3 furthest chunks (lowest similarity)
    bottom_3_indices = sorted_indices[-3:][::-1]  # Reverse to show least similar first

    # Print top 3 closest chunks with scores
    print("\n=== Top 3 Closest Chunks ===")
    for rank, idx in enumerate(top_3_indices, 1):
        chunk = chunks[idx]
        score = similarities[idx]
        print(f"\n{rank}. Score: {score:.4f}")
        print(f"   Source: {chunk['source_file']}, Chunk Index: {chunk['chunk_index']}")
        print(f"   Text: {chunk['text'][:200]}...")

    # Print top 3 furthest chunks with scores
    print("\n=== Top 3 Furthest Chunks ===")
    for rank, idx in enumerate(bottom_3_indices, 1):
        chunk = chunks[idx]
        score = similarities[idx]
        print(f"\n{rank}. Score: {score:.4f}")
        print(f"   Source: {chunk['source_file']}, Chunk Index: {chunk['chunk_index']}")
        print(f"   Text: {chunk['text'][:200]}...")

    # Prepare results for saving
    nearest_chunks = []
    for idx in top_3_indices:
        chunk = chunks[idx]
        nearest_chunks.append({
            "source_file": chunk["source_file"],
            "chunk_index": chunk["chunk_index"],
            "text": chunk["text"],
            "similarity_score": float(similarities[idx])
        })

    furthest_chunks = []
    for idx in bottom_3_indices:
        chunk = chunks[idx]
        furthest_chunks.append({
            "source_file": chunk["source_file"],
            "chunk_index": chunk["chunk_index"],
            "text": chunk["text"],
            "similarity_score": float(similarities[idx])
        })

    results = {
        "query": user_query,
        "nearest_chunks": nearest_chunks,
        "furthest_chunks": furthest_chunks
    }

    # Save results to JSON
    helpers.save_json(results, "outputs/task_9_retrieval_results.json")
