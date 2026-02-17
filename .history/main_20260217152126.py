import shutil
import os 


source_path=f'C:/Users/amanb/Downloads/'
destination_path='F:/05_Image_Art/'
os.chdir(source_path)
print(os.getcwd())

if 'Nano_banana' in os.listdir():
    

# if "Nano_Banana" in source_path:
#     print("File Found !")
# else:
#     print()

# shutil.move(source_path,destination_path)
# print(f"Moved '{source_path}' to '{destination_path}'")