import shutil
import os 


# filename=input("Enter the file name")
# source_path=f'C:/Users/amanb/Downloads/'
# destination_path='F:/05_Image_Art/'


def get_after_substring(s, delimiter):
    _, _, after_delim = s.partition(delimiter)
    return after_delim

def moveFilebulk(source_path,substring):
    os.chdir(source_path)
    print(os.getcwd())
    find=f"{source_path}/{substring}.png"

    # if substring in os.listdir():
    print("File Found ")
    print(os.getcwd)
    get_after_substring(source_path,"Nano_Banana")
    print(get_after_substring)
        # shutil.move(f"{source_path}/{get_after_substring}.png",destination_path)

    # else:
        # print('File not found !!')    

# if "Nano_Banana" in source_path:
#     print("File Found !")
# else:
#     print()
# ,substring,destination_path
# shutil.move(source_path,destination_path)
# print(f"Moved '{source_path}' to '{destination_path}'")


moveFilebulk('C:/Users/amanb/Downloads')