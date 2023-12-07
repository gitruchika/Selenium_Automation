import bdb

str1 = "Hello My name is mohit and my age is 25, live in Mumbai"
name = 'Rahul'
age = 30
city = 'Bangalore'

# 1. string concatenation with plus operator
str2 = "Hello My name is "+name+" and my age is " +str(age)+", live in " +city
print(str2)


# 2 : formating with format method
str3 = "Hello My name is {} and my age is {}, live in {}".format(name, age, city)
print(str3)

# 3: Fstring formatting
str4 = f"Hello My name is {name} and my age is {age}, live in {city}"
print(str4)

# Create a raw string
# \t : it represent the tab in string
# \n : it breaks the line
print("_"*50)
str5 = r"Hello \t\t Good Morning \n we are learning Python Programming"
print(str5)


# check given character is available in the string or not
"""
stra = "Python Programming is very easy to learn"
char = input("Enter string to check:")
if char in stra:
    print("This string is available :", char)
else:
    print("This string is not available :", char)
"""
print("_"*50)
# Apply loop on the string
strb = "Programming"
for char in strb:
    print(char)

# Apply loop with indexing
print("_"*50)
#len_str = len(strb)
for i in range(len(strb)):
    print(i, strb[i])


# count the total number of vowels
print("_"*40)
strc = "Please AconEnect to or crIeate"
vowels = "aeiou"
count = 0
for char in strc:
    if char in vowels:
        count = count + 1
    else:
        continue

print("Total vowels count :", count)

# Slicing in the string
print("_"*50)

strh = "Python Programming"
# Rule1 : str[initial index: last index]
# substring will include initial index, and exclude the last index
print(strh[1: 5])  # ytho

print(strh[2: -2]) # thon Programmi

print(strh[-5:-1]) # mmin

print(strh[-5: 2]) # No Output


print("_"*50)
# Rule 2 str[:last index]
# default initial index will be zero
strj = "Learning Python is fun"
print(strj[:5]) # Learn
print(strj[:-6]) # earning Python is fu

# print everything except first and last character
print(strj[1:-1]) # earning Python is fu

# print("_"*50)
# Rule3 : str[initial index:]
# by default last index will the end of the string
strk = "This will enable you to start turning"
print(strk[5:]) # will enable you to start turning

strg = "Programming"
print(strg[-4:]) # ming
print("_"*50)

# Rule4 : str[first index: last index: difference value]
str11= "Learning Python Programming"
print(str11[2: 12: 2]) # ann y

print(str11[1: 13: 3]) # engy

print(str11[5: 15: 2]) # igPto

# default initial index zero
print(str11[:18:3]) # LrnPh

# default last index : default last index is length of the string
str11= "Learning Python"
print(str11[4::2]) # nn yhn

# default last index and default index
print(str11[::3]) # LrnPh

# if difference value is negative, then default initial index will be -1 and last index will -len(string)
#       01234567
str11= "Learning Python"
#
print(str11[::-1]) # nohtyP gninraeL
# print(str11[-1:-15:-1])

print(str11[2::-1])
#print(str11[-15])

print("_"*40)
# expected : Virat is good player
qstr = "good player is Virat"

str1 = qstr[:12]
print(str1)
str2 = qstr[-5:]
print(str2)
str3 = qstr[12:14]
print(str3)

print(f"{str2} {str3} {str1}")

######################## String Methods ########

print(dir(str))
"""
  'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
  'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
  'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 
  'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
  'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
  'partition', 'removeprefix', 'removesuffix', 'replace', 
  'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 
  'rstrip', 'split', 'splitlines', 'startswith',
  'strip', 'swapcase', 'title', 'translate',
  'upper', 'zfill'
"""

# count method : This method return the count of any character or substring.
str22= "HeMiillo Good MornMiing"
print("o count :", str22.count('o')) # o count : 4
print("Mii count :", str22.count('Mii')) # Mii count : 2
print("space count :", str22.count(" ")) # space count : 2
print("count hello :", str22.count("hello")) # count hello : 0

# Find method : This method return index position if any given substring if
# it is available else it will return -1
str33 = "Today is very sunny day"
print("check very word :", str33.find("very")) # check very word : 9
print("check cool word :", str33.find("cool")) # check cool word : -1

# Index method: This method return the index position of given string if it
# is available, it will fail with value error
print("check very word :", str33.index("very"))
#print("check cool word :", str33.index("cool"))
#ValueError: substring not found

# upper : convert string to upper case
str4 = "Today iS Very Sunny Day"
print(str4.upper()) # TODAY IS VERY SUNNY DAY

# lower : convert string to lower case
print(str4.lower()) # today is very sunny day

# Swapcase : Convert lower case to upper and upper case to lower
print(str4.swapcase())
# tODAY Is vERY sUNNY dAY

# title : convert string in title, first character of each word should be capital
str5 = "today iS very SuNNy day"
print(str5.title())
# Today Is Very Sunny Day

# Capitalize: convert first character of string is Capital rest all lower case.
print(str5.capitalize())
# Today is very sunny day

# replace method:
print("_"*50)
str6 = "Pattern print Python is the best Python way to Learn"
result = str6.replace("Python", "Java")
print(result)

result2 = str6.replace("print", "PRINT").replace("best", "BEST")
print(result2)

# split method : This method helps to break the string with any of the character/string/substring.
print("_"*50)
str7 = "Programming"
split_Result = str7.split("r")
print(split_Result)

URL = "https://www.google.co.in"
url_split = URL.split(".")
print(url_split)
print(url_split[0])
result = url_split[0].split("//")
print(result)

# strip method : This method remove the trailing spaces (Begining and ending spaces.).
print("_"*50)
str13 = "  Hello Python  "
print(str13)
resul13 = str13.strip()
print(resul13)

#Program: Write a Python Program to find out the emails in the string.
"""
test_str = (" Pattern print is admin@gmail.com the best way to learn the python "
            "looping concept and fundamentals, test@gmail.com this post is a tribute to the Indian hockey team's win in Olympic 2020.")

word_list = test_str.split(" ")
print(word_list)
for word in word_list:
    #print(word)
    if "@" in word:
        print(word)
    else:
        continue
"""
# Program : Write a Python to get the count of each word
test_str = (" Pattern print is admin@gmail.com the best way to learn the python "
            "looping concept and fundamentals, test@gmail.com this post is a tribute to the Indian hockey team's win in Olympic 2020.")
word_list = test_str.split(" ")
for word in word_list:
    print(word, ":", test_str.count(word))

# Is methods.

# is upper
# is lower
# is title
# is digit
# is numeric
#

strj = 'Python'
strk = "PROGRAMMING"
print(strj.isupper()) # False
print(strk.isupper()) # True

strl = "python automation"
print(strl.islower()) # True

# check is title
strz = "Python Learning is Easy"
print(strz.istitle())

# check string has numeric
str12 = "3456723"
print(str12.isnumeric()) # True

str13 = "Hello 123"
print(str13.isnumeric()) # False

str14 = "Hello123"
print(str14.isalnum()) # True

# join method: this method join the string with any delimeters
#python -> p_y_t_h_o_n

result = "_".join("Python")
print(result) # P_y_t_h_o_n

result2 = "^&%".join("Programming")
print("result2 :", result2)
# result2 : P^&%r^&%o^&%g^&%r^&%a^&%m^&%m^&%i^&%n^&%g

str11 = "Good Morning"
delimeter = "+"
result11 = delimeter.join(str11)
print(result11)
# G+o+o+d+ +M+o+r+n+i+n+g

# Python program to check which are the word has vowels
str1 = "Pttern prnt is the btst wy to lrn the python"
vowels = "aeiou"
#1. split the string and get word_list
#2. loop on word list and the check
#3. if any word has vowels with then print the word
#4. else cotinue

# import pdb; pdb.set_trace()
word_list = str1.split()
print(word_list)
for word in word_list:
    for char in word:
        if char in vowels:
            print(word)
            break
        else:
            continue


# write a python program to get count of each word.
input_str = "Hello is good Morning, Python is good Language Hello Python"
#1. get word list with split method
#2. loop on each word
#3. get count of each word with input_str.count(word)
























































