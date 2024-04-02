import os 
import subprocess

process = subprocess.Popen(['echo', "More output output putttt"], stdout=subprocess.PIPE)
process2 = subprocess.run(['echo', 'Even more output puttt'], stdout=subprocess.PIPE, universal_newlines=True)

#stdout,stderr = process.communicate()

#print(process,stderr)
process2.stdout