import subprocess
!ldconfig -v
print(subprocess.run(["sh download_reqs_set_vars.sh"], shell=True))