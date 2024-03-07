
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI

llm = OpenAI()
chat_model = ChatOpenAI()

from langchain.schema import HumanMessage

text = "What would be a good company name for a company that makes colorful socks?"
messages = [HumanMessage(content=text)]

llm.invoke(text)
# >> Feetful of Fun

chat_model.invoke(messages)
# >> AIMessage(content="Socks O'Color")
# llm_response = llm.invoke(text)
# print("llm_response:", llm_response)

# chat_response = chat_model.invoke(messages)
# print("chat_response:", chat_response)
print("llm_response:", llm.invoke(text))
print("chat_response:", chat_model.invoke(messages))