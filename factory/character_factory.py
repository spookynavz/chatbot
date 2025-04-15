from services.character_services import Character   
from utils.prompt_loader import PromptLoader

class CharacterFactory:
    def __init__(self):
        self.loader = PromptLoader()

    def get_character(self, role: str):
       role = role.lower()
       prompt_template = self.loader.get_prompt(role)
       if not prompt_template:
            raise ValueError(f"No prompt found for role: {role}")
       return Character(prompt_template)
