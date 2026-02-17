import shutil
import os 
import sys


def moveFilestodestination(source_path,filenamesubstring,destination_path):
   
    os.chdir(source_path)
    for i in os.listdir():
        if filenamesubstring in  i:
            files=f"{source_path}{i}"
            print(files.replace('\\',"/"))
            shutil.move(files,destination_path.replace('\\',"/"))

moveFilestodestination()


if __name__ == "__main__":
      if len(sys.argv) > 1:
        user_argument = sys.argv[1]
        greet(user_argument)

