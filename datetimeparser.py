from langchain.output_parsers import DatetimeOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
output_parser = DatetimeOutputParser()
template = """Answer the users question:

{question}

{format_instructions}"""
prompt = PromptTemplate.from_template(
    template,
    partial_variables={"format_instructions": output_parser.get_format_instructions()},
)
# print(prompt)
chain = prompt | OpenAI() | output_parser
output = chain.invoke({"question": "elon musk got richer when?"})
print(output)