from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

load_dotenv()

model=ChatOpenAI()

chat_history= [
    SystemMessage(content="You are a helpful assistant.")
]

while True:
    user_input= input("You: ")
    if user_input == "exit":
        break
    chat_history.append(HumanMessage(content= user_input))
    response=model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print(response.content)

print(chat_history)


