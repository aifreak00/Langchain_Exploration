from langchain_openai import ChatOpenAI
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts.chat import ChatPromptTemplate
output_parser = CommaSeparatedListOutputParser()
print(output_parser.parse("hi, bye"))
# >> ['hi', 'bye']

