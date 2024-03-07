from langchain_openai import OpenAI

llm = OpenAI()
# response = llm.invoke(
#     "What are some theories about the relationship between unemployment and inflation?"
# )
# print(response)

for chunk in llm.stream(
    "What are some theories about the relationship between unemployment and inflation?"
):
    print(chunk, end="", flush=True)

# response=llm.batch(
#     [
#         "What are some theories about the relationship between unemployment and inflation?"
#     ]
# )
# print(response)

# import asyncio

# from langchain_openai import OpenAI

# async def main():
#     llm = OpenAI()
#     response = await llm.ainvoke("What are some theories about the relationship between unemployment and inflation?")
#     print(response)

# asyncio.run(main())

import asyncio

from langchain_openai import OpenAI  

async def main():
    llm = OpenAI()

    prompt = "What are some theories about the relationship between unemployment and inflation?"
    
    async for chunk in llm.astream(prompt): 
        print(chunk, end="", flush=True)

