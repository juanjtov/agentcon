# suppress warnings
import warnings

warnings.filterwarnings("ignore")

# import libraries
import requests, os
import textwrap
import tiktoken
import json
from pathlib import Path
import re

# dotenv
from dotenv import load_dotenv

load_dotenv()


class LlmModel:
    def __init__(
        self, model="meta-llama/Meta-Llama-3-8B-Instruct-Lite", provider="together"
    ):
        self.model = model
        self.total_cost = 0

        if provider == "together":
            import together

            self.client = together.Together(api_key=os.getenv("TOGETHER_API_KEY"))
        elif provider == "openai":
            import openai

            self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        elif provider == "openrouter":
            import openrouter

            self.client = openrouter.OpenRouter(api_key=os.getenv("OPENROUTER_API_KEY"))

    def parse_xml_tags(self, text, tags):
        """Parse specified XML tags from text and verify all tags are present."""
        result = {}
        missing = []
        for tag in tags:
            match = re.search(f"<{tag}>(.*?)</{tag}>", text, re.DOTALL)
            if match:
                result[tag] = match.group(1).strip()
            else:
                missing.append(tag)
        if missing:
            raise ValueError(f"Missing tags: {', '.join(missing)}")
        return result

    def parse_json_tags(self, text, tags):
        """Parse specified JSON tags from text and verify all tags are present."""
        result = {}
        missing = []
        for tag in tags:
            match = re.search(f'"{tag}": "(.*?)"', text, re.DOTALL)
            if match:
                result[tag] = match.group(1).strip()
            else:
                missing.append(tag)
        if missing:
            raise ValueError(f"Missing tags: {', '.join(missing)}")
        return result

    def prompt_llm(self, prompt, get_structured_output=None):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        output = response.choices[0].message.content

        if get_structured_output == "xml":
            return self.parse_xml_tags(output, get_structured_output)
        elif get_structured_output == "json":
            try:
                # Try to find JSON in the output
                json_match = re.search(r"\{.*\}|\[.*\]", output, re.DOTALL)
                if json_match:
                    return json.loads(json_match.group(0))
                return json.loads(output)
            except json.JSONDecodeError:
                # Fallback to tag parsing if generic JSON parsing fails
                # specific behavior for legacy/broken implementation compatibility
                return self.parse_json_tags(output, get_structured_output)
        return output


if __name__ == "__main__":
    ### Task 1: YOUR CODE HERE - Write a prompt for the LLM to respond to the user
    prompt = """
    what are the tourist attractions in morocco?
    
    Instructions:
    - 10 words max
    """

    # Get Response
    LLM = LlmModel(
        model="meta-llama/Meta-Llama-3-8B-Instruct-Lite", provider="together"
    )
    response = LLM.prompt_llm(prompt)

    print("\nResponse:\n")
    print(response)
    print("-" * 100)

    # save response under results/
    os.makedirs(".results", exist_ok=True)
    with open(".results/response.txt", "w") as f:
        f.write(response)
