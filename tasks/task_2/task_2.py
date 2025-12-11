import os
import helpers


def task_2():
    """
    Goal:
        Send an interesting prompt to an LLM and print the model response.
    Instructions:
        - Send an interesting prompt to an LLM
        - Print & save the model response to outputs/task_2.txt
    """
    # Initialize the LLM model
    llm = helpers.LlmModel(
        model="meta-llama/Meta-Llama-3-8B-Instruct-Lite", 
        provider="together"
    )
    
    # Create an interesting prompt
    prompt = """
    You are a creative storyteller. Write a very short (3-4 sentences) 
    sci-fi micro-story about an AI that discovers something unexpected 
    about the nature of consciousness. Make it thought-provoking and poetic.
    """
    
    # Get the response from the LLM
    response = llm.prompt_llm(prompt)
    
    # Print the response
    print("\n" + "="*60)
    print("LLM Response:")
    print("="*60)
    print(response)
    print("="*60 + "\n")
    
    # Save the response to outputs/task_2.txt
    helpers.save_txt(response, "outputs/task_2.txt")
    
    return response
