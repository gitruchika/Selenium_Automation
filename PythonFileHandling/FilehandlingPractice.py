"""
file = open(filename, filemode)
file.read()

Filemode :

read mode (r): This mode helps to read the content of the file
write mode (w): This mode helps to write or overwrite the existing of the file
append mode (a): This mode helps to add content at end of the file.

"""
# read file data
def read_file(filepath):
    file = open(filepath, "r")
    data = file.read()
    print("data :", data)
    file.close()

# read_file("read_data.txt") # read from current location
# read_file("E:\\Filesdata\\count_name.txt") # read from another directory


# Write content to the file
def write_content_to_file(filepath, content):
    file = open(filepath, "w")
    file.write(content)
    file.close()


# case 1: File doest not exiting : It will create new file with provided name and add content to the file
"""
str1 = "Hello Good Morning"
filename = "write_data.txt"
write_content_to_file(filename, str1)
"""

# case 2: File Already exist : It will overwrite the existing content of the file.
# filename2 = "write_content.txt"
# str2 = "Python is very easy to learn"
# write_content_to_file(filename2, str2)

### Append content to the file ####

def append_data_to_file(filepath, content):
    file = open(filepath, "a")
    file.write(content)
    file.close()


# case 1: File doest not exiting : It will create new file with provided name and add content to the file.
# str1 = "Python Programming Language\n"
# filename = "append_data.txt"
# append_data_to_file(filename, str1)


# case 2: File Already exist : It will content to the end of the file.
#str1 = "World cup 2023\n"
#filename = "append_data_new.txt"
#append_data_to_file(filename, str1)

#### Read specific number of character ###
def read_num_char(filepath, total_char):
    file = open(filepath, "r")
    data = file.read(total_char)
    print(data)
    file.close()


#read_num_char("read_data.txt", 30)

#### Read data line by line with context manager######

def read_line_by_line(filepath, line_num):
    with open(filepath, "r") as file:
      for i in range(line_num):
        data = file.readline()
        print(data)
        # data = file.readline()
        # print(data)
        # data = file.readline()
        # print(data)

#read_line_by_line("read_data.txt", 2)

# read list of lines

def read_all_lines(filepath):
    with open(filepath, "r") as file:
        data = file.readlines()
        return data


lines_list = read_all_lines("read_data.txt")
print("lines_list :", lines_list)

for i in range(-3, 0, 1):
    print(lines_list[i], end="")


# Write a python program to replace JAVA with PYTHON

def replace_words_in_files(filepath, word1, word2):
    with open(filepath, "r") as file:
        file_data = file.read()
        replace_data = file_data.replace(word1, word2)
        print(replace_data)

    with open(filepath, "w") as file:
        file.write(replace_data)

#replace_words_in_files("reaplce_data.txt", "JAVA", "PYTHON")


# Program to find out the list of emails from given file
print("_"*50)
def get_all_emails(filepath):
    with open(filepath) as file:
        file_data = file.read()
        word_list = file_data.split()
        for word in word_list:
            #print(word)
            if "@" in word:
                print(word)
            else:
                continue

#get_all_emails("email_data.txt")

# open file with r+

with open("read_data.txt", "r+") as file:
    file.write("Hello Good Morning")
    file_data = file.read()
    print(file_data)




















