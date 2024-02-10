import os 
import string

req_file=input("Enter your file name to search : ")
current_directory="/Users"
found_file=""

for r,d,f in os.walk(current_directory):
    for each_file in f:
        print("still checking in directory: "+r)
        
        if each_file == req_file:
            print("found it!!!")
            print("checking in directory : "+os.path.join(r, each_file))
            found_file = os.path.join(r, each_file)
            break

print("yeay, we found in : "+found_file)