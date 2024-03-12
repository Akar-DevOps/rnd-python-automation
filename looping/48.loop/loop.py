import os
import sys

path = input("Enter your directory path : ")
if os.path.exists(path):
    df_l = os.listdir(path)
else:
    print("please provide valid path..")
    sys.exit()

print("========")
print(df_l)

p1 = os.path.join(path, df_l[0])
p2 = os.path.join(path, df_l[1])

if os.path.isfile(p2):
    print(f"{p2} is a file")
else:
    print(f"{p2} is a directory")


for each in df_l:
    
    print("==========DIRECTORY / FILE CHECKING========")
    p3 = os.path.join(path, each)
    print(f"location : {p3}") 

    if os.path.isfile(p3):
        print(f"{p3} is a file")
    else:
        print(f"{p3} is a directory")
    
    print("==========/DIRECTORY / FILE CHECKING========")