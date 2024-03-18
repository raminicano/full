#!/bin/bash

# 첫 번째 인자를 이름으로, 두 번째 인자를 나이로 사용하여 인사 메시지를 출력하는 스크립트

if [ $# -eq 2 ]; then
  name="$1"
  age="$2"
  echo "안녕하세요, $name 님! 당신은 $age 세이군요."
else
  echo "사용법: ./script.sh 이름 나이"
fi
