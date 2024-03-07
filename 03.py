from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template("{foo}{bar}")
partial_prompt = prompt.partial(foo="ice")
print(partial_prompt.format(bar="cream"))

