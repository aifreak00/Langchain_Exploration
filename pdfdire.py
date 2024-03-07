from langchain_community.document_loaders import PyPDFDirectoryLoader
loader = PyPDFDirectoryLoader("/langchain/sample")
docs = loader.load()
print(len(docs))