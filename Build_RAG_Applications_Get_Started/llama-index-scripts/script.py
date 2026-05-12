import os
from llama_index.llms.openai_like import OpenAILike

# GitHub's API base for models
GITHUB_BASE_URL = "https://models.github.ai/inference"

llm = OpenAILike(
    model="deepseek/DeepSeek-V3-0324",              # Removed the "deepseek/" prefix
    api_key=os.environ["GITHUB_TOKEN"],
    api_base=GITHUB_BASE_URL,
    is_chat_model=True,
    temperature=0.7,
    max_tokens=1000,
    context_window=128000
)

response = llm.complete("Who is Laurie Voss?")
print(response)