from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

output_parser = CommaSeparatedListOutputParser()

format_instructions = output_parser.get_format_instructions()
prompt = PromptTemplate(
    template="List five {subject}.\n{format_instructions}",
    input_variables=["subject"],
    partial_variables={"format_instructions": format_instructions},
)

model = ChatOpenAI(temperature=0)

chain = prompt | model | output_parser
response=chain.invoke({"subject": "ice cream flavors with honey atleast 10"})
# print(response)
for s in chain.stream({"subject": "ice cream flavors with honey atleast 10"}):
    print(s)