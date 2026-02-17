import shutil
import os 
import argparse


def moveFilestodestination(source_path,filenamesubstring,destination_path):
   
    os.chdir(source_path)
    for i in os.listdir():
        if filenamesubstring in  i:
            files=f"{source_path}{i}"
            print(files.replace('\\',"/"))
            shutil.move(files,destination_path.replace('\\',"/"))



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A script to Move same type of file to the destination wanted.")
    parser.add_argument("source_path", type=str, help="Give the path of the source file :")
    parser.add_argument("filenamesubstring", type=str, help="Give the comman sub part in the files :")
    parser.add_argument("destination_path", type=str, help="Give the destination part")

    args = parser.parse_args()
    moveFilestodestination(args.source_path, args.filenamesubstring, args.destination_path)

