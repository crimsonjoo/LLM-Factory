import subprocess
import os

## webui에서 training 시작 시 만들어지는 yaml파일 사용

# 코드 추가 해야 할일
    # - 파라미터별로 변수를 받아, automatic하게 실행 할 것
    # - 변수를 yaml 저장 파일 위치로 받아, 파라미터 구간별로 계속해서 training 돌게 할것
    # - wandb 개인 계정 init() / apikey 연결하여서 위의 결과가 저장되도록 할것 (yml 파일에 report_to, run_name 자동 추가하도록 코드 작성)
    # - 자동으로 학습시킨 데이터명들을 wandb의 run_name으로 넘어가도록 설정
    # - 최초 입력해야 하는 파라미터명들을 한곳으로 모으기

#wandb 사용법
#회원가입 (개인계정으로 설정)
#터미널에서 로그인 (wandb login)
#training_args.yaml 파일에 코드 추가




# 필요한 명령어들을 순차적으로 실행합니다.
commands = [
    "ldconfig -v",
    "nvidia-smi",
    "pwd",
    "ls",
    "llamafactory-cli webui"
]

for command in commands:
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    if result.returncode != 0:
        print(f"Command failed with return code {result.returncode}: {command}")
        break