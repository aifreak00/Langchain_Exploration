from langchain.globals import set_llm_cache
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

from langchain.cache import InMemoryCache

set_llm_cache(InMemoryCache())

# The first time, it is not yet in cache, so it should take longer
print(llm.predict("Tell me a joke with elephants"))



# We can do the same thing with a SQLite cache
from langchain.cache import SQLiteCache

set_llm_cache(SQLiteCache(database_path=".langchain.db"))
%%time
# The first time, it is not yet in cache, so it should take longer
print(llm.predict("Tell me a joke"))