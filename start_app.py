import subprocess
import os

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