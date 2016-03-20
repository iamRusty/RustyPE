#Project Euler Maintenance Scripts
#V1 - Used to copy templates

import os
import shutil

_DEST_PATH = "C://Users//Rusty//Documents//Visual Studio Code//Project Euler//"
_SOURCE_PATH = "C://Users//Rusty//Documents//Visual Studio Code//Project Euler//try.py"

def main():
    print("Template Copier")
    folder = input("Input Folder:")
    _NEW_DEST_PATH = _DEST_PATH + str(folder) + "//try.py"
    if not os.path.exists(_NEW_DEST_PATH):
        shutil.copy(_SOURCE_PATH, _NEW_DEST_PATH)
    print("Done!")
    
main()