
from langchain_community.document_loaders.csv_loader import CSVLoader


# loader = CSVLoader(file_path='./example_data/mlb_teams_2012.csv')
# data = loader.load()
loader = CSVLoader("mlb_teams_2012.csv")
response = loader.load()
# print(response)
for document in response:
    print(document.page_content)

loader = CSVLoader(file_path='mlb_teams_2012.csv', csv_args={
    'delimiter': ',',
    'quotechar': '"',
    'fieldnames': ['MLB Team', 'Payroll in millions', 'Wins']
})

data = loader.load()
# # print(data)
for document in data:
      print(document.page_content)

loader = CSVLoader(file_path='mlb_teams_2012.csv', source_column="ml-Team")

data = loader.load()
# print(data)
for document in data:
     print(document.page_content)