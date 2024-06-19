# .PHONY는 실제 파일이 아닌 가상 타겟을 지정합니다.
.PHONY: all help clean

# SRCS 변수에 모든 .py 파일을 가져옵니다.
SRCS = $(wildcard *.py)

# PROGS 변수에 .py 확장자를 제거한 파일 이름을 저장합니다.
#PROGS = $(patsubst %.py, %, $(SRCS))
PROGS = $(SRCS:.py=)

# 기본 타겟 정의
all: $(PROGS)

# 각 파일을 실행하는 타겟을 정의합니다.
%: %.py
	streamlit run $<

# help 타겟 정의
help:
	@echo "Usage:"
	@echo "  make run your_file.py - Run the specified streamlit app"
	@echo "  make help              - Show this help message"
	@echo "  make clean             - Clean up generated files"

# clean 타겟 정의
clean:
	echo "Cleaning up..."
	rm -f *.pyc
	rm -rf __pycache__
