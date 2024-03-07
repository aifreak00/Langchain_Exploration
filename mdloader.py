from langchain_community.document_loaders import UnstructuredMarkdownLoader
markdown_path = 'readme.md'
loader = UnstructuredMarkdownLoader(markdown_path)
print(loader.load())
