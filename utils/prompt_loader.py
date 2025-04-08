import yaml

class PromptLoader:
    def __init__(self, file_path="templates/prompts.yaml"):
        with open(file_path, "r") as file:
            self.prompts = yaml.safe_load(file)

    def get_prompt(self, role: str):
        return self.prompts.get(role)
