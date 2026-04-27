from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os


temperature=1.0
max_token=10000
model_name= "openai/gpt-4.1-mini"
api_key=os.environ["GITHUB_TOKEN"]
model_url="https://models.github.ai/inference"


llm=ChatOpenAI(model=model_name,
               api_key=api_key,
               base_url=model_url,
               temperature=temperature,
               max_tokens=max_token)


devops_issues_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a troubleshooting assistant"),

    ("user", "Docker container not starting"),
    ("assistant", """
Root Cause: Port conflict
Fix:
1. Check running containers
2. Stop conflicting container
Command: docker ps
"""),

    ("user", "{issue}")
])

devops_issue=input("Enter your devops related issues :")
devops_issues_prompt_format=devops_issues_prompt.format(issue=devops_issue)

response=llm.invoke(devops_issues_prompt_format)
print(response.content)