import openai


prompt = 'A glamorous cat dancing on top of the Beat Education Center'


response = openai.Image.create(
  prompt=prompt,
  n=1
  )
image_url = response["data"][0]["url"]
print(image_url)


print(response)