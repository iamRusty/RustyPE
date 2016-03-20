#Project Euler Maintenance Script
#V1 - Used to create new folders

import os

_NUMBER_OF_DIRECTORIES = 50

def main():
    print("Folder Maker")
    default_path = "C://Users//Rusty//Documents//Visual Studio Code//Project Euler//"
    count = 1
    while (count <= _NUMBER_OF_DIRECTORIES):
        new_path = default_path + str(count)
        print(new_path)
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        count += 1
    print("Done!")
    
main()