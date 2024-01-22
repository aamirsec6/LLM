import os
from secret import OAI_KEY,SERP_KEY
os.environ["OPENAI_API_KEY"] = OAI_KEY
os.environ["SERPAPI_API_KEY"] = SERP_KEY

from langchain_openai import OpenAI

llm = OpenAI(temperature = 0.9)
name = llm("who will be the next prime minister of india 2024")
print(name)

from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])
chain = prompt | llm

chain.invoke({"input": "prime minister of france "})

from langchain_community.utilities import SerpAPIWrapper

search = SerpAPIWrapper()

print(search.run("Obama's first name?"))





