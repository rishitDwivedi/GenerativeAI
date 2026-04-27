from langchain_core.output_parsers import JsonOutputParser,CommaSeparatedListOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os


temperature=0.7
max_token=1000
model_name= "openai/gpt-4.1-mini"
api_key=os.environ["GITHUB_TOKEN"]
model_url="https://models.github.ai/inference"

json_parser=JsonOutputParser()
csv_parser= CommaSeparatedListOutputParser()

llm=ChatOpenAI(model=model_name,
           api_key=api_key,
           temperature=temperature,
           base_url=model_url,
           max_tokens=max_token,
           )

name_prompt_template = PromptTemplate.from_template(
    "My name in English is Spelled as {name}. Can you tell me the meaning of {name} in {language}. {format_instruction}"
)
name_prompt_template_csv=name_prompt_template.partial(format_instruction=csv_parser.get_format_instructions())
name_prompt_template_json=name_prompt_template.partial(format_instruction=json_parser.get_format_instructions())

name = input("Enter your Name: ")
name_lang=input("Your name is taken from which Language: ")
# name_prompt_format=name_prompt_template.format(name=name,language=name_lang)
llm_chain_csv=name_prompt_template_csv | llm | csv_parser
llm_chain_json=name_prompt_template_json | llm | json_parser
response_csv= llm_chain_csv.invoke({"name": name, "language": name_lang })
response_json= llm_chain_json.invoke({"name": name, "language": name_lang })

print("CSV Response",response_csv)
print("JSON Response",response_json)
