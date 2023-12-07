import os
import shutil

# get current working directory path
# print(os.getcwd()) # this will current location path
# E:\Trainings\PythonSelenium4Sept2023\OS_modules

# change the working directory
"""
print(os.getcwd())
os.chdir("E:\\Filesdata")
print(os.getcwd())
# E:\Filesdata
"""

# get list of all the files and folders

"""
list_dirs = os.listdir("E:\\Filesdata")
print(list_dirs)
# ['BE14', 'BI10', 'BI11', 'Bi12', 'BI13', 'BI14', 'Bi15', 'count_name.txt']
for data in list_dirs:
    print(data)

"""




# Create a directory on target location
"""
folder_path = "E:\\Filesdata\\BE14\\python_selenium"
os.mkdir(folder_path)
"""

# folder should be created on target directory

# Remove folder target directory
"""
os.removedirs("E:\\Filesdata\\BE14\\python_selenium")
"""

# get environment variable values
"""
result = os.getenv("path")
print("Result :", result)

print(os.getenv("Browser"))
print(result)


# run windows command using OS

os.system("notepad.exe")
os.system("control")
#os.system("python E:\\Trainings\\PythonSelenium4Sept2023\\PythonFileHandling\\Read_json_file_content.py")

# copy file from one location to another

src_path = "E:\\logs\\logfile.log"
tar_locate = "E:\\Filesdata\\BE14\\logfils_updated.log"
shutil.copy(src_path, tar_locate)

# Remove all the non empty directory from target location.
shutil.rmtree("E:\\Filesdata\\BE14")
# check given path is file or folder
"""

path1 = "E:\\Filesdata\\Bi12\\count_name_2.txt"
print(os.path.isfile(path1)) # True
print(os.path.isdir(path1))  #False

path2 = "E:\\Filesdata\\Bi12"
print(os.path.isdir(path2)) # True

# join two paths
path_a = "E:\\Filesdata\\Bi12"
file_name = "count_name_3.txt"

file_path = os.path.join(path_a, file_name)
print("file path :", file_path)















