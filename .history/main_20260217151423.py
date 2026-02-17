import shutil
import os 


source_path='C:/Users/amanb/Downloads/Nano_Banana_Pro_Make_1(9).png'
destination_path='F:/05_Image_Art/'

shutil.move(source_path,destination_path)
print(f"Moved '{source_path}' to '{destination_path}'")