!ldconfig -v
!nvidia-smi
import subprocess
import os
print(subprocess.run(["llamafactory-cli webui"], shell=True))