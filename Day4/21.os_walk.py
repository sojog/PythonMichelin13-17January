import os

current_directory = os.getcwd()

for dirpath, dirnames, filenames in os.walk(current_directory):
    print("dirpath:", dirpath)
    print("dirnames:", dirnames)
    print("filenames:", filenames)