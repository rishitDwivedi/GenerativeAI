import os
from pydantic import BaseModel
from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


class NameInfo(BaseModel):
    name: str
    meaning: str
    origin: str


output_parser=PydanticOutputParser(pydantic_object=NameInfo)

temperature=1.0
max_token=1000
model_name= "openai/gpt-4.1-mini"
api_key=os.environ["GITHUB_TOKEN"]
model_url="https://models.github.ai/inference"

llm=ChatOpenAI(model=model_name,
           api_key=api_key,
           temperature=temperature,
           base_url=model_url,
           max_tokens=max_token,
           )

name_prompt_template = PromptTemplate.from_template(
    """ My name is {name} and It is taken from {name_language} language.
        Tell me :
        - Meaning
        - Origin of the word
        {format_instruction}"""
)


name = input("Enter your Name: ")
name_lang=input("Your name is taken from which Language: ")
name_prompt_format=name_prompt_template.partial(format_instruction=output_parser.get_format_instructions())
llm_chain= name_prompt_format | llm | output_parser
response=llm_chain.invoke({"name": name,"name_language":name_lang})
print(response)