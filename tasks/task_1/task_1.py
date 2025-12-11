import helpers


def task_1():
    """
    This task ensures the environment is set up correctly.

    Instructions:
    - Install Python and dependencies
    - Run a script that generates a very cool looking hello world message

    Save the output to .results/task_1.txt.
    """
    text = "hello world"
    print(text)

    helpers.save_txt(text, ".results/task_1.txt")
