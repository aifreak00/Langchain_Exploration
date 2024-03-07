from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
loader = DirectoryLoader("/LANGCHAIN/sample", glob="**/*.txt" ,loader_cls=TextLoader)
docs = loader.load()
print(len(docs))

#/ necessary for retriveing the files the path we mention
from langchain_community.document_loaders import PythonLoader
loader = DirectoryLoader('/langchain', glob="**/*.py", loader_cls=PythonLoader)
docs = loader.load()
print(len(docs))