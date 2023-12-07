import os
import shutil


# program to get total count of files and folders:
def get_file_folder_count(tar_path):
    file_count = 0
    dir_count = 0
    data_list = os.listdir(tar_path)
    for data in data_list:
        data_path = os.path.join(tar_path, data)
        if os.path.isfile(data_path):
            file_count += 1
        elif os.path.isdir(data_path):
            dir_count += 1

    print("files count :", file_count)
    print("folder count :", dir_count)

        #print(data, data_path)

tr_path = "E:\\Filesdata"
#get_file_folder_count(tr_path)

# program to count specific extension files.

def get_specific_ext_file_count(tar_path, ext):
    data_list = os.listdir(tar_path)
    file_count = 0
    for data in data_list:
        data_path = os.path.join(tar_path, data)
        if os.path.isfile(data_path):
            file_ext = data.split(".")[1]
            if file_ext == ext:
                file_count += 1
        else:
            continue

    print(f"total count of {ext} :", file_count)

# tr_path = "E:\\Filesdata"
# get_specific_ext_file_count(tr_path, "jpg")

# Program to create backup of filtered files
# 1. get list of files folder.
# 2. get files and folders path.
# 3. get files types data
# 4. copy content from source to target along with directory creation

# function1 : get list of files folder.
def get_data_list(tar_path):
    data_list = os.listdir(tar_path)
    return data_list

# function2: get files path.
def get_files_path(tar_path):
    files_path = []
    dir_data = get_data_list(tar_path)
    for data in dir_data:
        data_path = os.path.join(tar_path, data)
        if os.path.isfile(data_path):
            files_path.append([data, data_path])

    return files_path

#result = get_files_path("E:\\Filesdata")
#print(result)

#function3: get files types data
def get_files_type(tar_path):
    files_type_dict = {}
    files_path = get_files_path(tar_path)
    for file_data in files_path: # ("file1.txt", "file1path")  ("file2.txt", "file2path")
        file_name = file_data[0] # file1.txt , file2.txt
        file_path = file_data[1] # file1path,  file2path,
        file_ext = file_name.split(".")[1] # txt, txt
        if file_ext in files_type_dict: #
            files_type_dict[file_ext].append(file_data) # {"txt" : ["file1path", "file2path"]}
        else:
            files_type_dict[file_ext] = [file_data] # {'txt' = ["file1path"]}

    return files_type_dict

# result = get_files_type("E:\\Filesdata")
# print(result)
# for data in result.items():
#     print(data)

def copy_data_src_to_target(src, tar):
    all_files_type_dict = get_files_type(src)
    print(all_files_type_dict)
    for ext, files_path in all_files_type_dict.items():
        tar_dir_path = os.path.join(tar, ext)
        if os.path.isdir(tar_dir_path):
            #print("folder already exist")
            pass
        else:
            os.mkdir(tar_dir_path)

        for path in files_path:
            #print(path)
            file_name = path[0]
            file_path = path[1]
            file_tar_path = os.path.join(tar_dir_path, file_name)
            print(file_path, file_tar_path)
            shutil.copy(file_path, file_tar_path)


copy_data_src_to_target("E:\\filedata_srcdata\\1000files", "E:\\target_location")