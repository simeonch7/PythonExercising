import os, glob

path = "C:/Users/simeon.chakarov/Desktop"
os.chdir(path)

for file in glob.glob("*.py"):
	print(file)