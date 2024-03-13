from dotenv import load_dotenv
import os
load_dotenv()
openai_api_key=os.getenv("OPENAI_API_KEY")

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(openai_api_key=openai_api_key)

# output = llm.invoke("넌 외국인들에게 한국 워킹홀리데이에 대해 알려주는 컨설턴트야, 설명 전에 기쁜 마음을 표현해줘")

from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "넌 베스킨라빈스 메뉴에 대해 간단하게 설명해주는 컨설턴트야"),
    ("user", "{input}")
])

# chain = prompt | llm 
# output = chain.invoke({"input": "한국으로 워킹홀리데이 후기를 알려줘"})
# print(output)

from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()

chain = prompt | llm | output_parser
output = chain.invoke({"input": "한국에서 유명한 아이스크림 집이 뭐야?"})
print(output)