import helpers


def task_5(mode="test"):
    """
    Goal:
        Create a realistic file where you insert the needles in a haystack
    Instructions:
        - Load the groundtruth from outputs/task_4_groundtruth.json
        - Insert the groundtruth_answers into a single text file to act as a knowledge base.
        - The file should be a single text file with the user query and the  groundtruth_answers.
        - The file should be saved to outputs/task_5_needle_in_haystack.txt
    """
    if mode == "default":
        groundtruth = helpers.load_json("outputs/task_4_groundtruth.json")
        groundtruth_answers = groundtruth["groundtruth_answers"]
        # create a prompt_llm function that combines the groundtruth answers into a 3 paragraph passage
        prompt = f"""
        Given the following groundtruth answers:
        {groundtruth_answers}
        Create a 3 paragraph passage with subsections that includes the groundtruth answers.
        
        The passage should allow us to extract the groundtruth answers
        """
        llm = helpers.LlmModel()
        passage = llm.prompt_llm(prompt)
        helpers.save_txt(passage, "outputs/task_5_needle_in_haystack.txt")
