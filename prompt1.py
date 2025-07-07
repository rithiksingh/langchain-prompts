from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()

model= ChatOpenAI(model="gpt-4")

template= "what is the capital of {country} ?"

prompt=PromptTemplate.from_template(template)
filled_prompt= prompt.invoke('india')
print(filled_prompt)



