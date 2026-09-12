import os
import shutil

fpath = input("Choose a Folder Path : ")

if os.path.exists(fpath):
    print("Path available!")
else:
    print("Sorry the path is not available :(")
    print("All folders & files:", os.listdir())