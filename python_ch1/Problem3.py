# using os module to print all file and directories

import os 

dir_path = "/" #add any file or folder name

#list all files and directories in the specified path
cont = os.listdir(dir_path)

#print each file and dircrtory name
for item in cont:
    print(item)