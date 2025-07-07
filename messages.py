from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

load_dotenv()

model=ChatOpenAI()

messages= [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of Italy?")
]

response=model.invoke(messages)

messages.append(AIMessage(content=response.content))

print(messages)