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
    pass

    llm = helpers.LlmModel()

    if mode == "predict":
        # 1. Extraction (Prediction)
        # test the insight extraction by loading the passage from the file
        user_query = helpers.load_json("outputs/task_4_groundtruth.json")["user_query"]
        passage = helpers.load_txt("outputs/task_5_needle_in_haystack.txt")
        prompt = f"""
        Given the following passage:
        {passage}
        
        
        Extract  3 insights from the passage in json format that addresses the user query {user_query}.
        Return the response in JSON format with two keys: 'insights' and 'justifications'.
        The insights should be the groundtruth answers and the justifications should be the justification for the answer.
        The response should be in the following format:
        {{
            "insights": [
                {{
                    "insight": "The groundtruth answer",
                    "justification": "The justification for the answer"
                }}
            ]
        }}
        """
        predicted_output = llm.prompt_llm(prompt, get_structured_output="json")
        print("Predicted Output:", json.dumps(predicted_output, indent=2))
        helpers.save_json(predicted_output, "outputs/task_5_insights.json")
    elif mode == "evaluate":
        # 2. Evaluation (LLM-as-a-Judge)
        user_query = helpers.load_json("outputs/task_4_groundtruth.json")["user_query"]
        groundtruth_data = helpers.load_json("outputs/task_4_groundtruth.json")
        groundtruth_answers = groundtruth_data["groundtruth_answers"]
        predicted_output = helpers.load_json("outputs/task_5_insights.json")
        # Extract just the insight text from the prediction for comparison
        predicted_insights_list = [
            item["insight"] for item in predicted_output.get("insights", [])
        ]

        evaluation_prompt = f"""
        You are an evaluator. 
        User Query: {user_query}
        
        Ground Truth Answers:
        {json.dumps(groundtruth_answers, indent=2)}
        
        Predicted Insights:
        {json.dumps(predicted_insights_list, indent=2)}
        
        Compare the predicted insights with the ground truth answers.
        Calculate the Recall score: (Number of correctly retrieved ground truth answers) / (Total number of ground truth answers).
        
        Provide a concise justification for the score.
        
        Return the output in JSON format:
        {{
            "recall_score": <float between 0 and 1>,
            "justification": "<string>"
        }}
        """

        evaluation_report = llm.prompt_llm(
            evaluation_prompt, get_structured_output="json"
        )

        # Save evaluation report
        helpers.save_json(evaluation_report, "outputs/task_6_evaluation_report.json")
        print("Evaluation Report:", json.dumps(evaluation_report, indent=2))
