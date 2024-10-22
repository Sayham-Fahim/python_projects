import os
import shutil

file_dir=r"folder path"

def catagory(folder):
    for file_name in os.listdir(folder):
        if os.path.isfile(os.path.join(folder,file_name)):
            file_ext=os.path.splitext(file_name)[1]
            if not os.path.exists(os.path.join(folder,file_ext)):
                os.makedirs(os.path.join(folder,file_ext))
            shutil.move(os.path.join(folder,file_name),os.path.join(folder,file_ext,file_name))

catagory(file_dir)