import os 

path="/Users/danakar/Documents/rizki-folder/rnd/python/python-automation/42.os.path.module"

print(os.walk(path)) # will error
print(list(os.walk(path)))

print("=========")

for r,d,f in os.walk(path):
    if len(f) != 0:
        # print directory
        print(r)
        for each_file in f:
            print(os.path.join(r, each_file))
        print("=========")