from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
response_schemas = [
    ResponseSchema(name="answer", description="answer to the user's question"),
    ResponseSchema(
        name="source",
        description="source used to answer the user's question, should be a website.",
    ),
]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
format_instructions = output_parser.get_format_instructions()
prompt = PromptTemplate(
    template="answer the users question as best as possible.\n{format_instructions}\n{question}",
    input_variables=["question"],
    partial_variables={"format_instructions": format_instructions},
)
model = ChatOpenAI(temperature=0)
chain = prompt | model | output_parser
response=chain.invoke({"question": "what's the capital of france?"})
print(response)