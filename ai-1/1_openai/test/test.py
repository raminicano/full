import json

with open('./VL_01. KAKAO/KAKAO_448_18.json', encoding='utf-8') as f:
    data = json.load(f)
for i in data["info"][0]['annotations']['lines']:
    

print(json.dumps(data, indent="\t", ensure_ascii=False))