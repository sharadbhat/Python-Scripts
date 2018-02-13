import sys
import psutil
import os
import time

file_name = sys.argv[0]

for pid in psutil.pids():
    p = psutil.Process(pid)
    if os.getpid() != pid:
        if p.name() == "python.exe" and len(p.cmdline()) > 1 and file_name in p.cmdline()[1]:
            print("Instance already running")
            sys.exit(0)

time.sleep(100) # Only for testing of script
