from langchain.prompts import PromptTemplate
prompt = (
    PromptTemplate.from_template("Tell me a joke about {topic}")
    + ", make it funny"
    + "\n\nand in {language}"
)
PromptTemplate(input_variables=['language', 'topic'], output_parser=None, partial_variables={}, template='Tell me a joke about {topic}, make it funny\n\nand in {language}', template_format='f-string', validate_template=True)
print(prompt.format(topic="sports", language="spanish"))

from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
model = ChatOpenAI()
chain = LLMChain(llm=model, prompt=prompt)
print(chain.run(topic="sports", language="spanish"))