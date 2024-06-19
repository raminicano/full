#!/bin/bash

# 인자로 받은 파일명을 변수에 할당
file=$1

# 파일명이 입력되었는지 확인
if [ -z "$file" ]; then
  echo "Usage: $0 <filename.py>"
  exit 1
fi

# 파일이 존재하는지 확인
if [ ! -f "$file" ]; then
  echo "Error: File '$file' not found."
  exit 1
fi

# Streamlit 실행
streamlit run "$file"
