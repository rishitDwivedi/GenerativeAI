import os
from langchain_openai import ChatOpenAI

mistral_model= "mistral-ai/mistral-small-2503"
llama_model= "meta/Meta-Llama-3.1-8B-Instruct"
openai_model= "openai/gpt-4.1-mini"
deepseek_model= "deepseek/DeepSeek-V3-0324"

api_key=os.environ["GITHUB_TOKEN"]
temperature=0.7
max_token=1000
llm_mistal= ChatOpenAI(model=mistral_model,
                       api_key=api_key,
                       base_url="https://models.github.ai/inference",
                       temperature=temperature,
                       )

llm_lama= ChatOpenAI(model=llama_model,
                       api_key=api_key,
                       base_url="https://models.github.ai/inference",
                       temperature=temperature,
                       max_tokens=max_token,
                       )

llm_openai= ChatOpenAI(model=openai_model,
                       api_key=api_key,
                       base_url="https://models.github.ai/inference",
                       temperature=temperature,
                       max_tokens=max_token,
                       )

llm_deepseek = ChatOpenAI(model=deepseek_model,
                       api_key=api_key,
                       base_url="https://models.github.ai/inference",
                       temperature=temperature,
                       max_tokens=max_token,
                       )

prompt = "Write one short joke about an ant and an elephant"
models= [llm_mistal,llm_lama,llm_openai,llm_deepseek]


for model in models:
    print("Model: ", model.model_name, "\n")
    print("Prompt: ",prompt)
    response=model.invoke(prompt)
    print("Response :",response.content, "\n")

print("Execution completed")