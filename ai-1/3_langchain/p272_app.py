from langchain.memory import ConversationSummaryMemory
from langchain.chat_models import ChatOpenAI

memory = ConversationSummaryMemory(
    llm=ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    ),
    max_token_limit=50,
    return_messages=True
)

memory.save_context({"input": "안녕"}, {"output": "하이룽"})
memory.save_context({"input": "라면 후루룩 먹으러갈래?"}, {"output" : "그래 좋아!"})
memory.save_context({"input" : "가보자고"}, {"output" : "그래"})

print(memory.load_memory_variables({}))