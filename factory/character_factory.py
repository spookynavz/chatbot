from services.character_services import Engineer, Doctor
from utils.prompt_loader import PromptLoader

class CharacterFactory:
    def __init__(self):
        self.loader = PromptLoader()

    def get_character(self, role: str):
        prompt_template = self.loader.get_prompt(role)
        if not prompt_template:
            raise ValueError(f"No prompt found for role: {role}")

        match role.lower():
            case "engineer":
                return Engineer(prompt_template)
            case "doctor":
                return Doctor(prompt_template)
            case _:
                raise ValueError(f"Unsupported role: {role}")
