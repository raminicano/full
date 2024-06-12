import openai

prompt = "집안에서 사랑받는 막내딸인 세영아가씨에 대해서 말해줘"

response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt,
    temperature=0,
    max_tokens=500
)

print(response["choices"][0]["text"])