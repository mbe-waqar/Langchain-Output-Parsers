from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatOpenAI()

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me the name, age , and occupation of the person you are describing. /n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# prompt = template.format()
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)

# print(final_result)

chain = template | model | parser
result = chain.invoke({})

print(result)
