import json
import textwrap
import os
import pickle

from .llm_model import LlmModel


def wrap_text(data):
    """
    Wrap the text to 80 characters
    """
    paragraphs = data.split("\n")
    wrapped_paragraphs = [textwrap.fill(p, width=80) for p in paragraphs]
    return "\n".join(wrapped_paragraphs)


def save_json(data, filename):
    """
    Save the data to a JSON file
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"\nSaved data to {filename}\n")


def load_json(filename):
    """
    Load the data from a JSON file
    """
    with open(filename, "r") as f:
        return json.load(f)


def save_txt(data, filename):
    """
    Save the data to a text file
    """
    data = wrap_text(data)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write(data)
    print(f"\nSaved data to {filename}\n")


def load_txt(filename):
    """
    Load the data from a text file
    """
    with open(filename, "r") as f:
        return f.read()


def save_pickle(data, filename):
    """
    Save the data to a pickle file
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "wb") as f:
        pickle.dump(data, f)
    print(f"\nSaved data to {filename}\n")


def load_pickle(filename):
    """
    Load the data from a pickle file
    """
    with open(filename, "rb") as f:
        return pickle.load(f)
