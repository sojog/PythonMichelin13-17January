# operating system
import os
from pprint import pprint

current_directory = os.getcwd()
print("The current directory is:", current_directory)
current_directory = current_directory + "/Day1"

all_files = os.listdir(current_directory)
print(type(all_files))


extensions = ["py", "ipynb"]

filtered_filed = []
for filename in all_files:
    if filename.endswith(extensions[0]) or filename.endswith(extensions[1]):
        filtered_filed.append(filename)

filtered_filed = sorted(filtered_filed)
print(filtered_filed)

files_to_rename = []
for filename in filtered_filed:
    if filename[1] == "." and filename[0].isnumeric():
        files_to_rename.append(filename)
print(files_to_rename)

for filename in files_to_rename:
    
    os.rename(current_directory + "/" + filename, current_directory + "/0" + filename)


os.rename("/Users/silviu/Documents/Bittnet/Michelin/PythonMichelin/Curs1-Python-grupa2/PythonMichelin13-17January/Day4/__test.py", "/Users/silviu/Documents/Bittnet/Michelin/PythonMichelin/Curs1-Python-grupa2/PythonMichelin13-17January/Day4/__test_renamed.py")
