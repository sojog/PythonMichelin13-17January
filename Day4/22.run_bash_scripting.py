import subprocess
import os

current_directory = os.getcwd()

old_file = f"{current_directory}/03.try_except.ipynb"
new_file = f"{current_directory}/03.try_except.py" 

command = f"ipynb-py-convert {old_file} {new_file}"

subprocess.Popen(command, shell=True)