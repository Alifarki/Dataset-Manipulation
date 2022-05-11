import os
import shutil

folder_path = r'E:/train/'
file_types = []
for file in (os.listdir(folder_path)):
    file_type_part_name_by_ = file.split('.')
    file_type = file_type_part_name_by_[0]
    if file_type not in file_types:
        file_types.append(file_type)
        path = os.path.join(folder_path, file_type)
        os.mkdir(path)
        path2=os.path.join(folder_path, file)
        shutil.move(path2, path)
    else:
        path=os.path.join(folder_path, file_type)
        path2=os.path.join(folder_path, file)
        shutil.move(path2, path)
"""بدست آوردن نام فایل مورد نظر از طریق تابع split و اندیس آن بدست آمده است"""