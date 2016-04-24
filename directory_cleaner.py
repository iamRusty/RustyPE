#   Project Euler Maintenance Scripts
#   V1 - Used to delete non-source code files
#        before pushing it to git

import os

def main():
    found = 0
    rootDir = '.'
    for dirName, subdirList, fileList in os.walk(rootDir):
        print('Found directory: %s' % dirName)
        for fname in fileList:
            if (fname.endswith('.exe') or fname.endswith('.class') or fname.endswith('.exe.stackdump') or fname.endswith('.stackdump')):
                found = 1
                os.remove(dirName + '\\' + fname)
                
    if (found):
        print("Done!")
    else:
        print("No non-source code file found")
        
main()