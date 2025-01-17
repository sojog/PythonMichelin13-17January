import subprocess
import os

current_directory = os.getcwd()
all_files = os.listdir(current_directory)


# install_command = "pip install ipynb-py-convert"
# subprocess.Popen(install_command, shell=True)

ipynb_files = []
for filename in all_files:
    if filename.endswith("ipynb"):
        ipynb_files.append(filename)


for filename in ipynb_files:
    old_file = f"{current_directory}/{filename}"
    new_file = f"{current_directory}/{filename}".replace("ipynb", "py") 

    command = f"ipynb-py-convert {old_file} {new_file}"

    subprocess.Popen(command, shell=True)