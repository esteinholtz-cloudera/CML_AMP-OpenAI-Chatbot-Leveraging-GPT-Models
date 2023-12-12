import subprocess

print(subprocess.run(["sh 0_session-install-deps/setup_chroma.sh"], shell=True))