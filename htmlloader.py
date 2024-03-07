# from langchain_community.document_loaders import UnstructuredHTMLLoader
# loader = UnstructuredHTMLLoader("savingfile.html")
# data = loader.load()
# print(data)
from langchain_community.document_loaders import BSHTMLLoader
loader = BSHTMLLoader("savingfile.html")
data = loader.load()
print(data)