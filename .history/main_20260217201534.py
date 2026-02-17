import shutil
import os 



def moveFilestodestination(source_path,filenamesubstring,destination_path):
   
    os.chdir(source_path)
    for i in os.listdir():
        if filenamesubstring in  i:
            files=f"{source_path}{i}"
            print(files)
            shutil.move(files,destination_path)

moveFilestodestination("C:/Users/amanb/Downloads/","Nano_Banana","F:/05_Image_Art/")

