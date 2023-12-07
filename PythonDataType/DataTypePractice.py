# Python Data Type
"""
1. Numbers:
    a). Integer
    b). Float
    c). Complex number
2. Sequencial:
    e). String
    f). List
    g). Tuple
3. Dictionary
4. Set
5. Boolean
"""

# Numbers : Numbers can be any numeric values which includes positive , negative, imaginary, pointer values.
# a). Integer:
"""
Properties:
-> Integer is immutable data type, once it is defined we can not change.
-> Integer can contain positive, negative and zero value.
"""
num1 = 1
num2 = 2345
num3 = 656464546456456564645645645
num4 = -456
num5 = 0

print(type(num1), type(num2), type(num3), type(num4), type(num5))

# b) Float: Any numeric value with pointers will be considered as float data type

var1 = 50.55
var2 = 60.765767567657567
var3 = 4354325435345.567788888
var4 = -56676.745654645
var5 = 0.0
var6 = 45.00

print(type(var1), type(var2), type(var3), type(var4), type(var5), type(var6))

#c) Complex number : Complex number is combination of real and imaginary number

temp1 = 50j + 20
print(type(temp1))
# 50j : Imaginary number
# 20 : real number

###########################
print("_"*50)
# Sequencial data type
# i) string

str1 = 'Hello'
str2 = 'K'
str3 = "Good Morning 1234"
str4 = """Python basic programs contains Python 
Programming Examples with all native Python 
data type, mathematical operations on Python 
Variables. Typecasting of Python Variables and 
get understanding of Python Fundamentals."""
str5 = ('Python basic programs contains Python '
        'Programming Examples with all native Python')

str6 = "443590438950843&^*&^*&^*&^*&^*&^*&0854390"

print("str4:", str4, type(str4))
print("str5:", str5, type(str5))
print("str1:", str1, type(str1))
print("str2:", str2, type(str2))
print("str3:", str3, type(str3))
print("str6:", str6, type(str6))


str7 = "Hello"

#  0  1   2  3  4  # Positive indexing
#  H  e   l  l  0
# -5 -4   -3 -2 -1 # Negative Indexing

print(str7[0]) # H
print(str7[-5]) # H
print(str7[2]) # l
print(str7[-3]) # l

"""
Properties:
-> String in immutable data Type
-> String follows the positive and negative indexing.
-> To define the string we have to enclose the data with quotes.
"""

#ii) List :
#        0    1    2        3   4   5
list1 = [23, 3.6, 'Python', 56, 78, 100]
#        -6  -5    -4       -3  -2  -1
print(list1, type(list1))
# [23, 3.6, 'Python', 56, 78] <class 'list'>

print(list1[2]) # get value with positive indexing
print(list1[-4]) # get value with negative indexing

# len function to get length any variable
print(len(list1))
list2 = [4, 6, 8, 2, 6, 7, 11]
list2.sort()
print(list2)
n = len(list2)
median_position = (n+1)//2

print("median of list2: ", list2[median_position-1])

list3 = [3, 4.5, 'Hello', [4, 6, 7], (4, 7, 8), {'a': 345, 'b' : 234}, {4, 7, 8}, True, None]
"""
Properties:
->  List is mutable data type, we can modify at any point of time.
-> List Can contains all type data, int, float, string, tuple, dict, bool, set.
->  List follows same positive and negative indexing  as like string.

"""
print(list3[4])
list3.append(60)
print(list3)

# Tuple Data Type:
"""
# Tuple is immutable data type, we can not change it once it is defined.
# Tuple can also contains all type of data as like list.
# Tuple Also follows the positive and negative indexing.
"""
#         0   1    2        3
tuple1 = (4, 6.6, 'Python', [4, 6, 7])
#         -4 -3    -2        -1
print(tuple1[-2])
print(tuple1[3], type(tuple1))
var1 = tuple1[3]
print(type(var1))
var2 = tuple1[-2]
print(type(var2))

###### dictinary #######
# dictionary data type store the data in the form of key value pair.
# {'key' : 'value'}
dict1 = {'Name' : 'Rahul', 'age': 45, 'email' : 'rahul@gmail.com', 'Name' : 'john'}
print(dict1, type(dict1)) # <class 'dict'>

print(dict1['age']) # 45
print(dict1['Name']) # john
"""
-> dict is a mutable data Type.
-> dict store the data in key value format.
-> Dict contains only unique key, duplicate keys are not allowed.
-> Only immutable data type can be key in the dict.
   int, float, string, bool, tuple
-> All Type of data can be value in the dictionary
"""

dict2 = {2 : 345, 5.6 : 'Hello', 'Python' : 'Programming', (2, 6, 8):
        'Hello', 'python': 'Its easy language to learn'}
print(dict2)


#### set data type ####
# set data type only store unique values.

set1 = {5, 7, 2, 8, 5, 'a', 'b', 'a'}
print(set1, type(set1))
# {2, 5, 'a', 7, 8, 'b'} <class 'set'>
"""
-> set is mutable data type.
-> set can only contains immutable data type, int, float, string,  tuple, bool
"""

set1.add((4, 7, 8))
print(set1)

#set1.add([6, 8, 2])
# print(set1)
# TypeError: unhashable type: 'list'

# set1.add({'a': 123, 'b' : 456})
# TypeError: unhashable type: 'dict'
print(dir(set))
#  'add', 'clear', 'copy', 'difference', 'difference_update',
#  'discard', 'intersection', 'intersection_update', 'isdisjoint',
#  'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
#  'symmetric_difference_update', 'union', 'update']

# Boolean Data Type :  Boolean data type can be defined with True and False
var1 = 40
var2 = 70
var4 = 70
print(var1 == var2) # False
var3 = True
print(var3, type(var3))
# True <class 'bool'>

print(var4 == var2) # True
print(var2 >= var1) # True















