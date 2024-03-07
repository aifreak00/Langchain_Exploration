from langchain.globals import set_llm_cache
from langchain_openai import ChatOpenAI
from langchain.cache import InMemoryCache, SQLiteCache
import time

llm = ChatOpenAI()

# Setting the cache to InMemoryCache
set_llm_cache(InMemoryCache())

# Measure the execution time for the first call
start_time = time.time()

# The first time, it is not yet in cache, so it should take longer
print(llm.predict("Tell me a joke with elephants"))

end_time = time.time()
execution_time_first_call = end_time - start_time
print("Execution time for the first call:", execution_time_first_call, "seconds")

# We can do the same thing with a SQLite cache
set_llm_cache(SQLiteCache(database_path=".langchain.db"))

# Measure the execution time for the second call
start_time = time.time()

# The first time, it is not yet in cache, so it should take longer
print(llm.predict("Tell me a joke"))

end_time = time.time()
execution_time_second_call = end_time - start_time
print("Execution time for the second call:", execution_time_second_call, "seconds")
