from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate


load_dotenv()

model= ChatOpenAI(model="gpt-4")

prompt=PromptTemplate(template="what is the capital of {country}",
                      input_variables=['country'])


#fill the prompt
filled_prompt=prompt.invoke({'country':'India'})

print(filled_prompt)