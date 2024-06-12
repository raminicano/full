import openai
import numpy as np
import faiss

in_text = "야바문의 정체를 골라라"

response = openai.Embedding.create(
    model="text-embedding-ada-002",
    input=in_text
)

in_embeds = [record["embedding"] for record in response["data"]]
in_embeds = np.array(in_embeds).astype("float32")

target_text = [
    "문준현",
    "피더문",
    "초대우교",
    "국제고",
    "프리미어더 한나"
]


response = openai.Embedding.create(
    model="text-embedding-ada-002",
    input=target_text
)

target_embeds = [record["embedding"] for record in response["data"]]
target_embeds = np.array(target_embeds).astype("float32")

index = faiss.IndexFlatL2(1536)
index.add(target_embeds)

d, i = index.search(np.array(in_embeds).astype("float32"), 1)
print(d)
print(i)
print(target_text[i[0][0]])