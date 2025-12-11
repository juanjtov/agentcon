import helpers
import tiktoken
from sentence_transformers import SentenceTransformer


def chunk_text(text, chunk_size=64, overlap=12):
    """
    Chunk text into chunks of specified token size with overlap.
    """
    encoder = tiktoken.get_encoding("cl100k_base")
    tokens = encoder.encode(text)
    
    chunks = []
    start = 0
    while start < len(tokens):
        end = start + chunk_size
        chunk_tokens = tokens[start:end]
        chunk_text = encoder.decode(chunk_tokens)
        chunks.append(chunk_text)
        start += chunk_size - overlap  # Move forward by (chunk_size - overlap)
    
    return chunks


def task_8():
    """
    Goal:
        Chunk the three needle-in-haystack files, embed every chunk, and save the data for retrieval.
    Instructions:
        - Load the three needle-in-haystack files from the outputs/task_7_file_1.txt, outputs/task_7_file_2.txt, and outputs/task_7_file_3.txt
        - Chunk the three files into chunks of 64 tokens with 12 token overlap
        - Embed each chunk using Sentence Transformers
        - Save the chunks and embeddings to the outputs/task_8_chunks.json and outputs/task_8_embeddings.pkl
    """

    # Load the three needle-in-haystack files
    file_paths = [
        "outputs/task_7_file_1.txt",
        "outputs/task_7_file_2.txt",
        "outputs/task_7_file_3.txt",
    ]
    
    # Process each file and collect all chunks with metadata
    all_chunks = []
    for file_path in file_paths:
        text = helpers.load_txt(file_path)
        chunks = chunk_text(text, chunk_size=64, overlap=12)
        
        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "source_file": file_path,
                "chunk_index": i,
                "text": chunk
            })
    
    print(f"Total chunks created: {len(all_chunks)}")
    
    # Embed each chunk using Sentence Transformers
    model = SentenceTransformer("all-MiniLM-L6-v2")
    chunk_texts = [chunk["text"] for chunk in all_chunks]
    embeddings = model.encode(chunk_texts)
    
    print(f"Embeddings shape: {embeddings.shape}")
    
    # Save chunks to JSON
    helpers.save_json(all_chunks, "outputs/task_8_chunks.json")
    
    # Save embeddings to pickle
    helpers.save_pickle(embeddings, "outputs/task_8_embeddings.pkl")
