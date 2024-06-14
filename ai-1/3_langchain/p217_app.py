import langchain
from langchain.llms import OpenAI
## 특정 LLM의 캐시 비활성화

llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    temperature=0,
)

llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    cache=False
)

print(llm.generate(["오늘 너의 마음을 색깔로 표현해줘"]))

print(llm.generate(["오늘 너의 마음을 색깔로 표현해줘"]))