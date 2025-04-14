from string import Template

class Character:
    def __init__(self, prompt_template: dict):
        self.prompt_start = prompt_template["prompt_start"]
        self.input_variables = prompt_template["input_variables"]

    def respond(self, **kwargs):
        missing = [var for var in self.input_variables if var not in kwargs]
        if missing:
            raise ValueError(f"Missing input variables: {', '.join(missing)}")

        template = Template(self.prompt_start)
        return template.safe_substitute(**kwargs)