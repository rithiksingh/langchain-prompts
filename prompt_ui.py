from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

#set the model for llm
model= ChatOpenAI(model="gpt-4")

st.header('Research Tool')

user_input= st.text_input('Enter your prompt')

# if button is clicked
if st.button('Summmarize'):
    result=model.invoke(user_input)
    st.write(result.content)