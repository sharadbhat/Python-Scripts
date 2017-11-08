import os
import shutil

base_address = "C:/Users/Sharad/Documents/Github/"

os.chdir(base_address)

for x in os.walk(base_address):
    if x[0].endswith("__pycache__"):
        shutil.rmtree(x[0])
