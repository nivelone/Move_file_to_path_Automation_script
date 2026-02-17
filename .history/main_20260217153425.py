import shutil
import os 


# filename=input("Enter the file name")
# source_path=f'C:/Users/amanb/Downloads/'
# destination_path='F:/05_Image_Art/'




def moveFilebulk(source_path,substring,destination_path):
    os.chdir(source_path)
    print(os.getcwd())
    find=f"source_path/substring"
    if substring in os.listdir():
        print("File Found ")
        print(os.getcwd)
        print()
        shutil.move(source_path,destination_path)

    else:
        print('File not found !!')    

# if "Nano_Banana" in source_path:
#     print("File Found !")
# else:
#     print()

# shutil.move(source_path,destination_path)
# print(f"Moved '{source_path}' to '{destination_path}'")