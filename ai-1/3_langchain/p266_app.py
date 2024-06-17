from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
memory.chat_memory.add_user_message("배고프다")
memory.chat_memory.add_user_message("강남역 근처에서 뭐먹을까?")
memory.chat_memory.add_user_message("서브웨이 먹을까?")
memory.chat_memory.add_user_message("그러면 배달 시켜먹자")
memory.chat_memory.add_user_message("오케이 지금 함께배달 한다.")
memory.chat_memory.add_user_message("그랭")

print(memory.load_memory_variables({}))