import os

curdir = os.getcwd()

#get filename from curdir path
filename = os.path.basename(curdir)
print("Filename: ", filename)
