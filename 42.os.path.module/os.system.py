import os

os.listdir()
os.system("pwd")
os.system("ls")

cmd="date"
rt=os.system(cmd)

# will return 0 if rt is working
if rt==0:
    print("your cmd was successfully executed")
else:
    print("your command was failed")