# from langchain_community.chat_models import ChatAnthropic
# chat = ChatAnthropic(model="claude-2")
# for chunk in chat.stream("hi hello"):
#     print(chunk.content, end="", flush=True)
# from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
chat = ChatOpenAI(model="gpt-3.5-turbo")

for chunk in chat.stream("justin bieber songs "):
    print(chunk.content, end="", flush=True)