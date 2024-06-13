import json
import os
import re




# 디렉토리와 파일 경로 설정
directory = '/work/full/ai-1/1_openai/test/VL_01. KAKAO'
output_directory = 'output'
combined_json_file = 'combined.json'


# 출력 디렉토리 생성
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# 모든 JSON 파일 목록 가져오기
json_files = [file for file in os.listdir(directory) if file.endswith('.json')]

# 합친 데이터를 저장할 리스트
combined_data = []

# 각 JSON 파일 읽기 및 합치기
for json_file in json_files:
    input_file = os.path.join(directory, json_file)
    
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        combined_data.extend(data["info"][0]['annotations']['lines'])

# 합친 데이터 저장
with open(os.path.join(output_directory, combined_json_file), 'w', encoding='utf-8') as outfile:
    json.dump(combined_data, outfile, ensure_ascii=False, indent=4)

