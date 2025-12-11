import helpers
import json


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
        - Provide structured output where each insight has a justification and citation (source file)
        - Evaluate recall using the same LLM-driven evaluation prompt from Task 6
    """

    # Load groundtruth data (user query and groundtruth answers)
    groundtruth = helpers.load_json("outputs/task_4_groundtruth.json")
    user_query = groundtruth["user_query"]
    groundtruth_answers = groundtruth["groundtruth_answers"]
    
    # Load chunks and embeddings
    chunks = helpers.load_json("outputs/task_8_chunks.json")
    embeddings = helpers.load_pickle("outputs/task_8_embeddings.pkl")
    
    # Load retrieval results
    retrieval_results = helpers.load_json("outputs/task_9_retrieval_results.json")
    nearest_chunks = retrieval_results["nearest_chunks"]
    furthest_chunks = retrieval_results["furthest_chunks"]
    
    # Combine retrieved chunks for context
    context_chunks = []
    
    # Add 3 most similar chunks
    print("\n=== 3 Most Similar Chunks ===")
    for chunk in nearest_chunks:
        context_chunks.append({
            "source": chunk["source_file"],
            "text": chunk["text"],
            "type": "similar",
            "score": chunk["similarity_score"]
        })
        print(f"Source: {chunk['source_file']}, Score: {chunk['similarity_score']:.4f}")
    
    # Add 3 most different chunks
    print("\n=== 3 Most Different Chunks ===")
    for chunk in furthest_chunks:
        context_chunks.append({
            "source": chunk["source_file"],
            "text": chunk["text"],
            "type": "different",
            "score": chunk["similarity_score"]
        })
        print(f"Source: {chunk['source_file']}, Score: {chunk['similarity_score']:.4f}")
    
    # Build context string for the LLM
    context_text = ""
    for i, chunk in enumerate(context_chunks, 1):
        context_text += f"\n--- Chunk {i} (Source: {chunk['source']}, Type: {chunk['type']}, Score: {chunk['score']:.4f}) ---\n"
        context_text += chunk["text"]
        context_text += "\n"
    
    # Create LLM instance
    llm = helpers.LlmModel()
    
    # Generate improved answer with citations
    generation_prompt = f"""You are an expert at synthesizing information from multiple sources to answer user queries.

USER QUERY: {user_query}

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
    "summary": "A brief overall summary of how households can reduce peak energy consumption",
    "insights": [
        {{
            "insight": "The specific insight or recommendation",
            "justification": "Why this insight is relevant and helpful",
            "source_file": "The source file where this information was found"
        }}
    ]
}}

Return ONLY valid JSON, no other text.
"""
    
    # Get LLM response with structured output
    print("\n=== Generating Improved Answer with Citations ===")
    response = llm.prompt_llm(generation_prompt, get_structured_output="json")
    
    # Save the structured response as JSON
    helpers.save_json(response, "outputs/task_10_response.json")
    
    # Format as text for task_10.txt
    output_text = f"""IMPROVED ANSWER WITH CITATIONS
{'='*60}

USER QUERY: {user_query}

{'='*60}
SUMMARY
{'='*60}

{response.get('summary', 'No summary provided')}

{'='*60}
DETAILED INSIGHTS WITH CITATIONS
{'='*60}

"""
    
    insights = response.get('insights', [])
    for i, insight_data in enumerate(insights, 1):
        output_text += f"""
INSIGHT {i}:
{insight_data.get('insight', 'N/A')}

JUSTIFICATION:
{insight_data.get('justification', 'N/A')}

SOURCE: {insight_data.get('source_file', 'N/A')}

{'-'*40}
"""
    
    # Save improved answer to task_10.txt
    helpers.save_txt(output_text, "outputs/task_10.txt")
    
    # ============================================================
    # EVALUATE RECALL using the same LLM-driven evaluation from Task 6
    # ============================================================
    
    print("\n=== Evaluating Recall ===")
    
    # Extract predicted insights from the response
    predicted_insights = [insight_data.get('insight', '') for insight_data in insights]
    
    # Evaluate recall using LLM-as-a-Judge
    evaluation_results = []
    covered_count = 0
    
    for gt_answer in groundtruth_answers:
        # Create evaluation prompt for each groundtruth answer
        eval_prompt = f"""You are an expert evaluator assessing whether predicted insights cover a groundtruth answer.

USER QUERY: {user_query}

GROUNDTRUTH ANSWER: {gt_answer}

PREDICTED INSIGHTS:
{json.dumps(predicted_insights, indent=2)}

Task: Determine if any of the predicted insights semantically covers the groundtruth answer.
The insight doesn't need to be word-for-word identical, but should convey the same core meaning.

Respond with a JSON object in this exact format:
{{
    "is_covered": true or false,
    "matching_insight": "the insight that covers this answer (or null if none)",
    "reasoning": "brief explanation of your judgment"
}}
"""
        
        result = llm.prompt_llm(eval_prompt, get_structured_output="json")
        
        evaluation_results.append({
            "groundtruth_answer": gt_answer,
            "is_covered": result.get("is_covered", False),
            "matching_insight": result.get("matching_insight"),
            "reasoning": result.get("reasoning", "")
        })
        
        if result.get("is_covered", False):
            covered_count += 1
    
    # Calculate recall
    recall = covered_count / len(groundtruth_answers) if groundtruth_answers else 0
    
    # Create evaluation report
    evaluation_report = {
        "user_query": user_query,
        "num_groundtruth_answers": len(groundtruth_answers),
        "num_predicted_insights": len(predicted_insights),
        "num_covered": covered_count,
        "recall": recall,
        "predicted_insights": predicted_insights,
        "evaluation_details": evaluation_results
    }
    
    # Save evaluation report as JSON
    helpers.save_json(evaluation_report, "outputs/task_10_evaluation_report.json")
    
    # Append evaluation results to task_10.txt
    eval_text = f"""

{'='*60}
RECALL EVALUATION REPORT
{'='*60}

Groundtruth Answers: {len(groundtruth_answers)}
Predicted Insights: {len(predicted_insights)}
Covered Answers: {covered_count}
RECALL: {recall:.2%}

{'='*60}
EVALUATION DETAILS
{'='*60}
"""
    
    for i, result in enumerate(evaluation_results, 1):
        status = "✅ COVERED" if result["is_covered"] else "❌ NOT COVERED"
        eval_text += f"""
Groundtruth Answer {i}: {status}
Answer: {result["groundtruth_answer"]}
Matching Insight: {result["matching_insight"] if result["matching_insight"] else "None"}
Reasoning: {result["reasoning"]}
{'-'*40}
"""
    
    # Append to task_10.txt
    with open("outputs/task_10.txt", "a") as f:
        f.write(eval_text)
    
    print(f"\n{'='*60}")
    print("TASK 10 COMPLETE")
    print(f"{'='*60}")
    print(f"Generated {len(predicted_insights)} insights with citations")
    print(f"Groundtruth Answers: {len(groundtruth_answers)}")
    print(f"Covered Answers: {covered_count}")
    print(f"RECALL: {recall:.2%}")
    print(f"{'='*60}")
    
    return {
        "response": response,
        "evaluation_report": evaluation_report
    }
