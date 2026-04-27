import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


temperature=0.7
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
    "My name in English is Spelled as {name}. Can you tell me the meaning of {name} in {language}."
)

name = input("Enter your Name: ")
name_lang=input("Your name is taken from which Language: ")
name_prompt_format=name_prompt_template.format(name=name,language=name_lang)
response=llm.invoke(name_prompt_format)
print(response.content)


