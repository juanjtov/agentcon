import helpers
import json


def task_6(mode="evaluate"):
    """
    Goal:
        Evaluate the Recall of the Insight extraction using LLM-as-a-Judge (Predict and Evaluate)
    Instructions:
        - Load the user query from the file outputs/task_4_groundtruth.json
        - Load the groundtruth answers from the file outputs/task_4_groundtruth.json
        - Load the predicted insights from the file outputs/task_5_insights.json
        - Evaluate the recall of the predicted insights using the groundtruth answers
        - Save the evaluation report to the file outputs/task_6_evaluation_report.json
    """
    # Load groundtruth data
    groundtruth = helpers.load_json("outputs/task_4_groundtruth.json")
    user_query = groundtruth["user_query"]
    groundtruth_answers = groundtruth["groundtruth_answers"]
    
    if mode == "predict":
        # Extract insights from the haystack document
        haystack_content = helpers.load_txt("outputs/task_5_needle_in_haystack.txt")
        
        # Create LLM instance
        llm = helpers.LlmModel()
        
        # Prompt to extract insights from the haystack
        extract_prompt = f"""You are an expert at extracting relevant insights from documents.

Given the following user query and document, extract all relevant insights that answer the query.

USER QUERY: {user_query}

DOCUMENT:
{haystack_content}

Instructions:
- Extract all insights from the document that are relevant to answering the user query
- Each insight should be a complete, self-contained answer
- Return your response as a JSON array of strings
- Only include insights that directly address how households can reduce peak energy consumption

Return ONLY a JSON array in this format:
["insight 1", "insight 2", "insight 3", ...]
"""
        
        # Get predicted insights from LLM
        predicted_insights = llm.prompt_llm(extract_prompt, get_structured_output="json")
        
        # Save predicted insights
        insights_data = {
            "user_query": user_query,
            "predicted_insights": predicted_insights
        }
        helpers.save_json(insights_data, "outputs/task_5_insights.json")
        
        print(f"\nExtracted {len(predicted_insights)} insights from the document")
        print("\nPredicted Insights:")
        for i, insight in enumerate(predicted_insights, 1):
            print(f"  {i}. {insight[:100]}...")
        
        return insights_data
    
    elif mode == "evaluate":
        # Load predicted insights
        try:
            insights_data = helpers.load_json("outputs/task_5_insights.json")
            predicted_insights = insights_data["predicted_insights"]
        except FileNotFoundError:
            print("Error: Predicted insights not found. Run with mode='predict' first.")
            return None
        
        # Create LLM instance for evaluation
        llm = helpers.LlmModel()
        
        # Evaluate recall using LLM-as-a-Judge
        # For each groundtruth answer, check if it's covered by any predicted insight
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
            "evaluation_details": evaluation_results
        }
        
        # Save evaluation report as JSON
        helpers.save_json(evaluation_report, "outputs/task_6_evaluation_report.json")
        
        # Generate markdown report
        md_report = f"""# Evaluation Report - Recall Assessment

## Overview

| Metric | Value |
|--------|-------|
| **User Query** | {user_query} |
| **Groundtruth Answers** | {len(groundtruth_answers)} |
| **Predicted Insights** | {len(predicted_insights)} |
| **Covered Answers** | {covered_count} |
| **Recall** | {recall:.2%} |

---

## Predicted Insights

"""
        for i, insight in enumerate(predicted_insights, 1):
            md_report += f"{i}. {insight}\n"
        
        md_report += """
---

## Evaluation Details

"""
        for i, result in enumerate(evaluation_results, 1):
            status = "✅ Covered" if result["is_covered"] else "❌ Not Covered"
            md_report += f"""### Groundtruth Answer {i}

**Status:** {status}

**Groundtruth:** {result["groundtruth_answer"]}

**Matching Insight:** {result["matching_insight"] if result["matching_insight"] else "None"}

**Reasoning:** {result["reasoning"]}

---

"""
        
        # Save markdown report
        with open("outputs/task_6_evaluation_report.md", "w") as f:
            f.write(md_report)
        print(f"\nSaved markdown report to outputs/task_6_evaluation_report.md\n")
        
        print(f"\n{'='*60}")
        print("EVALUATION REPORT - Recall Assessment")
        print(f"{'='*60}")
        print(f"User Query: {user_query}")
        print(f"Groundtruth Answers: {len(groundtruth_answers)}")
        print(f"Predicted Insights: {len(predicted_insights)}")
        print(f"Covered Answers: {covered_count}")
        print(f"RECALL: {recall:.2%}")
        print(f"{'='*60}")
        
        return evaluation_report
