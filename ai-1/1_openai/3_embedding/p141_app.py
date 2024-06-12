import openai

text = "테스트 입니다."

response = openai.Embedding.create(
    model="text-embedding-ada-002",
    input=[text]
)

print(len(response["data"][0]["embedding"]))
print(response["data"][0]["embedding"])