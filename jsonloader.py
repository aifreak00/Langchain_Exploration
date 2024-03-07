from langchain_community.document_loaders import JSONLoader
import json 
from pathlib import Path
from pprint import pprint


# file_path='sample3.json'
# data = json.loads(Path(file_path).read_text())
# print(data)

loader = JSONLoader(
    file_path='sample3.json1',
    jq_schema='.messages[].content',
    text_content=False)

data = loader.load()
pprint(data)