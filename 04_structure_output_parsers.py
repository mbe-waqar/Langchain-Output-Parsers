from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatOpenAI()

schema = [
    ResponseSchema(name='fact1', description='fact 1 about the topic'),
    ResponseSchema(name='fact2', description='fact 2 about the topic'),
    ResponseSchema(name='fact3', description='fact 3 about the topic'),
]