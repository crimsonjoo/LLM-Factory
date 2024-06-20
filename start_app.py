!ldconfig -v
!nvidia-smi
import subprocess
import os

!cd LLaMA-Factory
print(subprocess.run(["llamafactory-cli webui"], shell=True))