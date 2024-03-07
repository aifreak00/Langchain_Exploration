# from langchain_community.document_loaders import TextLoader

# loader = TextLoader("emart_docker-compose.txt")
# response=loader.load()
# print(response)
# from langchain_community.document_loaders import TextLoader

# loader = TextLoader("emart_docker-compose.txt")
# response = loader.load()

# # Check the type and attributes of the first element in the list
# first_element = response[0]
# print(type(first_element))
# print(dir(first_element))

# # Assuming 'page_content' is an attribute of the first element
# if 'page_content' in dir(first_element):
#     print(first_element.page_content)
# else:
#     print("page_content attribute not found.")
from langchain_community.document_loaders import TextLoader

loader = TextLoader("emart_docker-compose.txt")
response = loader.load()
print(response)
for document in response:
    print(document.page_content)
