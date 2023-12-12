import subprocess
import os

## Use this script to RUN Chroma hosted
print(subprocess.run(["chroma run --path /home/cdsw/chroma-data --port " + str(os.environ['CDSW_APP_PORT'])], shell=True))