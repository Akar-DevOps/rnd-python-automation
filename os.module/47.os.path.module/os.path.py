import os 

path = input("Enter your path : ")

if os.path.exists(path):
    print(f"Given path : {path} is a valid path")

    if os.path.isfile(path):
        print(f" and it is a file path")
    else:
        print(f" and it is a directory path")

else:
    print(f"Given path : {path} is not exist on this host")