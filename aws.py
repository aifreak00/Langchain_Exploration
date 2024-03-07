from langchain_community.document_loaders import AmazonTextractPDFLoader
loader = AmazonTextractPDFLoader("emotion.jpg")
documents = loader.load()