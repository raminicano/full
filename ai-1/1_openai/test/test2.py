import json

with open('./output/combined.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

output_jsonl_file = 'test.jsonl'

def convert_to_new_format(old_data):
    new_data = []
    for i in range(len(old_data) - 1):
        user_entry = old_data[i]
        assistant_entry = old_data[i + 1]

        new_entry = {
            "messages": []
        }
        
        user_content = user_entry['norm_text']
        assistant_content = assistant_entry['norm_text']

        if user_entry['id'] % 2 != 0:  # 홀수
            new_entry["messages"].append({"role": "user", "content": user_content})
            new_entry["messages"].append({"role": "assistant", "content": assistant_content})
        else:  # 짝수
            new_entry["messages"].append({"role": "assistant", "content": user_content})
            new_entry["messages"].append({"role": "user", "content": assistant_content})

        new_data.append(new_entry)

    return new_data

# 데이터 변환
converted_data = convert_to_new_format(data)

# 변환된 데이터를 JSONL 형식으로 저장
with open(output_jsonl_file, 'w', encoding='utf-8') as file:
    for entry in converted_data:
        file.write(json.dumps(entry, ensure_ascii=False) + '\n')