from string import Template

class BaseCharacter:
    def __init__(self, prompt_template: dict):
        self.prompt_start = prompt_template["prompt_start"]
        self.input_variables = prompt_template["input_variables"]

    def respond(self, **kwargs):
        template = Template(self.prompt_start)
        return template.safe_substitute(**kwargs)

class Engineer(BaseCharacter):
    pass

class Doctor(BaseCharacter):
    pass
