import os
import signal
import sys
from time import sleep

#launch cmd
value = os.system("start cmd.exe @cmd /c pip install -r ../code/Digi-sm/requirements.txt")

#wait for requirements to install   
while True:
    sleep(1)
    if value == 0:
        break

if sys.argv[2] == "virgin":
    os.system("start cmd.exe @cmd /k python ../code/Digi-sm/run.py -create")
elif sys.argv[2] == "dummy":
    os.system("start cmd.exe @cmd /k python ../code/Digi-sm/run.py -dummy")
else:
    os.system("start cmd.exe @cmd /k python ../code/Digi-sm/run.py")

#kill tkinter
os.kill(int(sys.argv[1]), signal.SIGTERM)
#kill script once cmd is closed
os.kill(os.getpid(), signal.SIGTERM)
