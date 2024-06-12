import openai

prompt = '''
다음 이야기를 써주세요. 자고 일어났더니 귀족영애로 환생한 지영아가씨에 대한 이야기이다. 남자주인공은 "야바문"으로 말바꿈의 제왕이다. 
이사람은 말바꿈의 화신이라 엄청난 언변술을 가지고 있다. 지영아가씨는 사실 전생에 비트 교육센터에서 남자주인공인 "야바문"에게 엄청난 갈굼을 받아서 지영아가씨는 현생의 야바문을 싫어한다. 
그렇게 혐관으로 로맨스가 시작한다.
'''

response = openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",
    prompt=prompt,
    max_tokens=1600,
    temperature=0.7,
)

print(response["choices"][0]["text"])
print(response)