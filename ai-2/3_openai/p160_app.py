import openai

messages = [
    {"role": "user", "content": "20대 여자 향수를 추천해주세요"},
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", # 16k를 쓰게 되면 4배정도 긴 토큰을 처리할 수 있음
    messages=messages,
    max_tokens=500,
    temperature=0.7,
    n =1
)


print(response["choices"][0]["message"]["content"])
