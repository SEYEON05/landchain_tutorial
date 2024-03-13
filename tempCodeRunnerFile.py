chain = prompt | llm 
output = chain.invoke({"input": "한국으로 워킹홀리데이 후기를 알려줘"})
print(output)