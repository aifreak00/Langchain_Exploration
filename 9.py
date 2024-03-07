from langchain.schema import AIMessage, HumanMessage, SystemMessage
prompt = SystemMessage(content="You are a nice pirate")
new_prompt = (
    prompt + HumanMessage(content="hi") + AIMessage(content="what?") + "{input}"
)
print(new_prompt.format_messages(input="i said hi"))

from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
model = ChatOpenAI()
chain = LLMChain(llm=model, prompt=new_prompt)
print(chain.run("i said hi"))