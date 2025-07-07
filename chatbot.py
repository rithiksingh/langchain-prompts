from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

load_dotenv()

model=ChatOpenAI()

messages= [
    SystemMessage(content="You are a helpful assistant.")
]

while True:
    

