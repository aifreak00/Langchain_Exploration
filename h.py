import pprint
from typing import Any, Dict

import pandas as pd
from langchain.output_parsers import PandasDataFrameOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
model = ChatOpenAI(temperature=0)
# Solely for documentation purposes.
def format_parser_output(parser_output: Dict[str, Any]) -> None:
    for key in parser_output.keys():
        parser_output[key] = parser_output[key].to_dict()
    return pprint.PrettyPrinter(width=87, compact=True).pprint(parser_output)
# Define your desired Pandas DataFrame.
df = pd.DataFrame(
    {
        "num_legs": [2, 4, 8, 0],
        "num_wings": [2, 0, 0, 0],
        "num_specimen_seen": [10, 2, 1, 8],
    }
)

# Set up a parser + inject instructions into the prompt template.
parser = PandasDataFrameOutputParser(dataframe=df)

# Here's an example of a column operation being performed.
# df_query = "Retrieve the average of the num_legs column from rows 1 to 3."

# # Set up the prompt.
# prompt = PromptTemplate(
#     template="Answer the user query.\n{format_instructions}\n{query}\n",
#     input_variables=["query"],
#     partial_variables={"format_instructions": parser.get_format_instructions()},
# )

# chain = prompt | model | parser
# parser_output = chain.invoke({"query": df_query})

# format_parser_output(parser_output)

# Here's an example of a row operation being performed.
# df_query = "Retrieve the first row."

# # Set up the prompt.
# prompt = PromptTemplate(
#     template="Answer the user query.\n{format_instructions}\n{query}\n",
#     input_variables=["query"],
#     partial_variables={"format_instructions": parser.get_format_instructions()},
# )

# chain = prompt | model | parser
# parser_output = chain.invoke({"query": df_query})

# format_parser_output(parser_output)

# Here's an example of a random Pandas DataFrame operation limiting the number of rows
# df_query = "Retrieve the average of the num_legs column from rows 1 to 3."

# # Set up the prompt.
# prompt = PromptTemplate(
#     template="Answer the user query.\n{format_instructions}\n{query}\n",
#     input_variables=["query"],
#     partial_variables={"format_instructions": parser.get_format_instructions()},
# )

# chain = prompt | model | parser
# parser_output = chain.invoke({"query": df_query})

# print(parser_output)
# Here's an example of a random Pandas DataFrame operation limiting the number of rows
df_query = "Retrieve the average of the num_legs column ."

# Set up the prompt.
prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser
parser_output = chain.invoke({"query": df_query})

print(parser_output)