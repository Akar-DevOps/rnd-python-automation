import os
path="/Users/danakar/Documents/rizki-folder/rnd/python/python-automation/42.os.path.module/os.path.py"

print(os.path.basename(path))
print(os.path.dirname(path))

print("================")
path1="/Users"
path2="danakar"
print(path1+path2)
print("join string : "+path1+"/"+path2)
print("join with os.path : "+os.path.join(path1,path2))



print("=======split path======")
print(os.path.split(path))

print("=====get size======")
print(os.path.getsize(path))

print("==========exist========")
if os.path.exists(path):
  print("your file is there")
else:
  print(f'{path} is not present on this host')


print("========is file======")
if os.path.isfile(path):
  print(f"{path} is a file")
else:
  print(f"{path} is a dir")

print("==========myos")
print("Checking os : ")
print(os.path.islink("myos"))
print(os.path.islink("os.path.py"))
