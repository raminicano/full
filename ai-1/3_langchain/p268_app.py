from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(k=3, return_messages=True)
memory.save_context({"input": "안녕"}, {"output": "하이룽"})
memory.save_context({"input": "배고파"}, {"output": "그래?"})
memory.save_context({"input": "밥먹자"}, {"output": "그래"})

print(memory.load_memory_variables({}))