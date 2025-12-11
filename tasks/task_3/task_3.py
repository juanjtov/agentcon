import json
import helpers


def task_3():
    """
    Goal:
        Provide a paragraph and extract three insights with justifications using a structured prompt.

    Instructions:
        - Load the data from data/christmas.txt
        - Provide 3 insights about the passage as a list, where each insight includes a justification.
        - Return the response in JSON format with two keys: 'passage' (containing the text) and 'insights' (a list of objects with 'insight' and 'justification' keys).
        - Save the structured output nicely (in markdown format) to outputs/task_3.txt.
    """
    # Load the passage from data/christmas.txt
    passage = helpers.load_txt("data/christmas.txt")
    
    # Initialize the LLM model
    llm = helpers.LlmModel(
        model="meta-llama/Meta-Llama-3-8B-Instruct-Lite",
        provider="together"
    )
    
    # Create a structured prompt to extract insights
    prompt = f"""Analyze the following passage and extract exactly 3 insights with justifications.

PASSAGE:
{passage}

INSTRUCTIONS:
- Provide exactly 3 insights about the passage
- Each insight should have a clear justification based on the text
- Return your response as valid JSON with this exact structure:

{{
  "passage": "<the original passage text>",
  "insights": [
    {{"insight": "<insight 1>", "justification": "<justification 1>"}},
    {{"insight": "<insight 2>", "justification": "<justification 2>"}},
    {{"insight": "<insight 3>", "justification": "<justification 3>"}}
  ]
}}

Return ONLY the JSON, no additional text."""

    # Get raw response from the LLM (don't use built-in JSON parsing due to newline issues)
    response = llm.prompt_llm(prompt)
    
    # Clean the response - replace newlines within JSON strings
    import re
    # Find JSON block in response
    json_match = re.search(r"\{.*\}", response, re.DOTALL)
    if json_match:
        json_str = json_match.group(0)
        # Replace literal newlines with spaces (except between JSON elements)
        # This handles newlines within string values
        cleaned_json = re.sub(r'(?<=[^,\[\{])\n(?=[^\]\}])', ' ', json_str)
        cleaned_json = cleaned_json.replace('\n', ' ')
        result = json.loads(cleaned_json)
    else:
        raise ValueError("No JSON found in LLM response")
    
    # Ensure the passage is included in the result
    if "passage" not in result or not result["passage"]:
        result["passage"] = passage
    
    # Print the structured output
    print("\n" + "="*60)
    print("Extracted Insights:")
    print("="*60)
    print(json.dumps(result, indent=2))
    print("="*60 + "\n")
    
    # Create markdown formatted output
    markdown_output = f"""# Christmas Passage Analysis

## Original Passage

{result.get('passage', passage)}

## Insights

"""
    
    for i, item in enumerate(result.get("insights", []), 1):
        markdown_output += f"""### Insight {i}

**Insight:** {item.get('insight', 'N/A')}

**Justification:** {item.get('justification', 'N/A')}

"""
    
    # Save the markdown output
    helpers.save_txt(markdown_output, "outputs/task_3.txt")
    
    return result
