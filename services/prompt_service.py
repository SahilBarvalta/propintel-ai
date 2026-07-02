from pathlib import Path


def load_prompt():

    BASE_DIR = Path(__file__).resolve().parent.parent

    prompt_path = BASE_DIR / "prompts" / "advisor.txt"

    with open(prompt_path, "r") as file:

        return file.read()