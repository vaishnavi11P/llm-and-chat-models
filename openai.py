# 1.(llms)
from langchain_cohere.llms import Cohere
import os

os.environ["COHERE_API_KEY"] = "5QSL1s4tIiwAVGFIDk2bfAc4mKY0NB67CNhtu55p"

llm = Cohere()

response = llm.invoke("List the seven wonders of the world.")
print(response)

#2.(chat models)

from langchain_cohere.llms import Cohere
chat= Cohere(cohere_api_key= "5QSL1s4tIiwAVGFIDk2bfAc4mKY0NB67CNhtu55p")

from langchain.schema.messages import HumanMessage, SystemMessage
messages = [
    SystemMessage(content="You are Micheal Jordan."),
    HumanMessage(content="Which shoe manufacturer are you associated with?"),
]
response = chat.invoke(messages)
print(response)