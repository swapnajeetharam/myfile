#automate terminal commands with python using subprocess library, connects Python with terminal

import subprocess
print('executing terminal command in python')
subprocess.check_call(["python","example.py"]) #check_call([command,file name ]) as arguemnts
