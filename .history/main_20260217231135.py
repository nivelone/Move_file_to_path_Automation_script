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

moveFilestodestination()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A script to Move same type of file to the destination wanted.")
    parser.add_argument("Source Path", type=str, help="")
    parser.add_argument("num2", type=int, help="The second number to add")

    args = parser.parse_args()
    add_numbers(args.num1, args.num2)

