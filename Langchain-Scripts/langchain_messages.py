import os
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI


deepseek_model= "deepseek/DeepSeek-V3-0324"
api_key = os.environ["GITHUB_TOKEN"]

temperature=1.0
tokens=1000
url="https://models.github.ai/inference"

deepseek_llm=ChatOpenAI(model=deepseek_model,
                        base_url=url,
                        temperature=temperature,
                        max_tokens=tokens,
                        api_key=api_key,
                        )

sys_msg_1=SystemMessage("You are a doctor with 15  years of experience. Answer the questions accordingly?")
human_msg_1=HumanMessage("From where do the children comes on earth?")
msgs=[sys_msg_1,human_msg_1]
response=deepseek_llm.invoke(msgs)
print(response.content)
