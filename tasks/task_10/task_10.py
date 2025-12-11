def task_10():
    """
    Goal:
        Combine retrieved chunks with the user query and generate an improved answer using the LLM with citations and evaluate the recall of the answer.
    Instructions:
        - Load the user query from the file outputs/task_4_groundtruth.json
        - Load the chunks and embeddings from the outputs/task_8_chunks.json and outputs/task_8_embeddings.pkl
        - Load the retrieval results from the outputs/task_9_retrieval_results.json
        - Combine the user query with the 3 most similar chunks and the 3 most different chunks
        - Generate an improved answer using the LLM
        - Save the improved answer to the outputs/task_10.txt
    """
    pass
