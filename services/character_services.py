from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

class Character:
    def __init__(self, prompt_template: dict):
        self.prompt_text = prompt_template["prompt_start"]
        self.input_variables = prompt_template["input_variables"]
        self.llm = ChatOpenAI(temperature=0, model_name="deepseek-r1") 

    def respond(self, question, context=""):
        prompt = PromptTemplate(
            template=self.prompt_text,
            input_variables=["question", "context"]
        )
        chain = prompt | self.llm
        return chain.invoke({"question": question, "context": context})