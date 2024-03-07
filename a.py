import json

from langchain_core.utils.function_calling import convert_to_openai_tool


def multiply(a: int, b: int) -> int:
    """Multiply two integers together.

    Args:
        a: First integer
        b: Second integer
    """
    return a * b


print(json.dumps(convert_to_openai_tool(multiply), indent=2))

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo")
print(llm.invoke("what's 5 times three", tools=[convert_to_openai_tool(multiply)]))