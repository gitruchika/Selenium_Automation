"""
-> dict store the data in form of key value pair
-> dict only contains unique key, duplicate key is not allowed.
-> dict can contain any type of data as value, int, float, string, list, tuple, dict e.tc.
-> dict only consider the immutable data type as key, int, float, string, tuple, Boolean
"""
#         key       value
dict1 = {'name' : 'John'}
print(dict1['name'])

dict1[123] = 'Hello'
dict1[3.5] = [5, 7, 8]
dict1['Python'] = (66, 77, 88)
dict1[(1, 2, 3)] = {'a' : 123, 'b' : 567}

print(dict1)

input_dict = {'name': 'John', 123: 'Hello', 3.5: [5, 7, 8], 'Python': (66, 77, 88), (1, 2, 3): {'a': 123, 'b': 567}}

print(input_dict[3.5][1]) # 7

print(input_dict[(1, 2, 3)]['a']) # 123

print(input_dict[123][2]) # l

# apply loop on the dict data
print("_"*40)
for val in input_dict:
    print(val)
"""
123
3.5
Python
(1, 2, 3)
"""

for val in input_dict.items():
    print(val)
"""
('name', 'John')
(123, 'Hello')
(3.5, [5, 7, 8])
('Python', (66, 77, 88))
((1, 2, 3), {'a': 123, 'b': 567})
"""
print("_"*50)
for key, val in input_dict.items():
    print("Key :", key)
    print("value :", val)

print("_"*40)
dict11 = {'name' : 'Aditya', 'age' : 25, 'email' : 'adi@gmail.com', 'phone' : 4534566}
print(dict11['phone'])


for key, value in dict11.items():
    if key == 'phone':
        print(value)
    else:
        continue

school = {
    '9th' : [
        {'name': 'rahul', 'email' : 'rahul@gmail.com', 'phone': 54645645},
        {'name': 'rahul1', 'email' : 'rahul1@gmail.com', 'phone': 5443435645},
        {'name': 'rahul2', 'email' : 'rahul2@gmail.com', 'phone': 533444455},
    ],
  '10th' : [
        {'name': 'john', 'email' : 'john@gmail.com', 'phone': 98797897},
        {'name': 'john1', 'email' : 'john1@gmail.com', 'phone': 55333666},
        {'name': 'john2', 'email' : 'john2@gmail.com', 'phone': 232322323},
    ]
}


print(school['10th'][2]['phone'])

class_name = '10th'
st_name = 'john2'

for key, value in school.items():
    # print("key :", key)
    # print("value :", value)
    if key == class_name:
        print("key :", key)
        print("value :", value)
        st_list = value
        for st in st_list:
            #print(st)
            if st['name'] == st_name:
                print(st['phone'])


print("_"*40)
# dictionary methods
print(dir(dict))

"""
'clear', 'copy', 'fromkeys', 'get', 
'items', 'keys', 'pop', 'popitem', 
'setdefault', 'update', 'values'
"""

# Add data to the dict
dict1 = {'a': 456, 'b':123}

dict1['c'] = 600

print(dict1)

# update : This method update one dict data to another dictionary.
dicta = {'name' : 'john', 'age': 40, 'email': 'john@gmail.com'}
dictb = {'address' : 'Mumbai', 'phone': 9980890890}
dicte = {'country' : 'India', 'continent' : 'Asia'}

dicta.update(dictb)
print(dicta)
dicta.update(dicte)
print(dicta)


# read data from dict
dictj = {'name': 'john', 'age': 40, 'email': 'john@gmail.com', 'address': 'Mumbai', 'phone': 9980890890, 'country': 'India', 'continent': 'Asia'}
print(dictj['address'])

# get method
var1 = dictj.get('phone')
print("var1 :", var1)

# remove data from dictionary
# pop method: This method remove data from dict using key and it returns the value of the key.

var2 = dictj.pop('email')
print("var2 :", var2)

print("dictj :", dictj)

# popitem: This method remove the last key pair added in the dict.
#          It returns the data in the key value format enclose with tuple.
dictk = {'name': 'john', 'age': 40, 'address': 'Mumbai', 'phone': 9980890890, 'country': 'India', 'continent': 'Asia'}
var3 = dictk.popitem()

print("var3:", var3) # var3: ('continent', 'Asia')
print("dictk :", dictk)
# dictk : {'name': 'john', 'age': 40, 'address': 'Mumbai', 'phone': 9980890890, 'country': 'India'}

# clear method: This method remove all the data from dict and only empty dictionary will available
dicty = {'a': [3, 6, 7],
         'b' : 467,
         'c' : 1001}
dicty.clear()
print(dicty) # {}

# del method
dictz = {'a': [3, 6, 7],
         'b' : 467,
         'c' : 1001,
         'd' : 777}

del dictz['a']
print("dictz :", dictz)
# dictz : {'b': 467, 'c': 1001, 'd': 777}

del dictz # delete the dictionary from memory
# print("dictz :", dictz)
# name 'dictz' is not defined. Did you mean


# get list of keys:

dictv = {'a': [3, 6, 7],
         'b' : 467,
         'c' : 1001,
         'd' : 777,
         'e' : 6666,
         'f' : 1020}

print(dictv.keys())
# dict_keys(['a', 'b', 'c', 'd', 'e', 'f'])

# Get list values
print(dictv.values())
# dict_values([[3, 6, 7], 467, 1001, 777, 6666, 1020])


# get list of keys and in form of tuple
print(dictv.items())
# dict_items([('a', [3, 6, 7]), ('b', 467), ('c', 1001), ('d', 777), ('e', 6666), ('f', 1020)])

#### copy method ####

# shallow copy
print("_"*40)
dictv = {'aa': [3, 6, 7],
         'bb' : 467,
         'cc' : 1001,
         'dd' : 777,
         'ee' : 6666,
         'ff' : 1020}
dicth = dictv

dicth['gg'] = 2023
print("dicth :", dicth)
print("dictv :", dictv)

# Deep copy

dictq = {'aa': [3, 6, 7],
         'bb' : 467,
         'cc' : 1001,
         'dd' : 777,
         'ee' : 6666,
         'ff' : 1020}

dictr = dictq.copy()
dictr['hh'] = 7070
print("_"*40)
print("dictq :", dictq)
print("dictr :", dictr)


# setdefault method : This method assign default value to the keys which are available in the target dict.
print("_"*50)
dictq = {'aa': [3, 6, 7],
         'bb' : 467,
         'cc' : 1001,
         'dd' : 777,
         'ee' : True,
         'ff' : 1020,
         'gg' : 200}

# use the key which not available in dict
output = dictq.setdefault('jj', 800)
print(output) # 800

# use the key which is available in dict
output2 = dictq.setdefault('ee', 900)
print(output2) # True

#### fromkeys method  ####

dictq = {'aa': [3, 6, 7],
         'bb' : 467,
         'cc' : 1001,
         'dd' : 777,
         'ee' : True,
         'ff' : 1020,
         'gg' : 200}

result = dictq.fromkeys(['sal1', 'sal2', 'sal3', 'Hello'], 500)
print(result)
# {'sal1': 500, 'sal2': 500, 'sal3': 500, 'Hello': 500}

print("_"*60)
# program1: write a python program to print desire output
str1 = "Hello Good Morning"
#dict1 = {'H' : 'olleH', 'G' : 'dooG', 'M' : 'gninroM'}

output = {}
word_list = str1.split()
for word in word_list:
    first_char = word[0]
    revers_word = word[::-1]
    output[first_char] = revers_word

print("output :", output)
#output : {'H': 'olleH', 'G': 'dooG', 'M': 'gninroM'}


#porgram2 : create the dictinary with given string
str1= "Python Programming Language"
# output = {'Pn' : 'ytho', 'Pg': 'rogrammin', 'Le' : 'anguag'}

"""
12). Python Dictionary program to sort a dictionary in python using values.
Input = {‘d’ : 14, ‘b’ : 52,  ‘a’: 13, ‘c’: 1 }
Output= (c, 1) (a,13) (d, 14) (b, 52)
"""

Input_dict = {"d" : 14, "b" : 52,  "a": 13, "c": 1 }
print(Input_dict.items())
result1 = {key:value for key, value in sorted(Input_dict.items(), key= lambda item : item[1])}
# {'c': 1, 'a': 13, 'd': 14, 'b': 52} : sort on the basis of values
print(result1)

result2 = {key:value for key, value in sorted(Input_dict.items(), key= lambda item : item[0])}
# {'a': 13, 'b': 52, 'c': 1, 'd': 14} : sort on the basis of keys
print(result2)


print("_"*40)
list1 = [('d', 14), ('b', 52), ('a', 13), ('c', 1)]
print(sorted(list1, key= lambda item: item[1]))
print(sorted(list1))

#####################################

#20). Python Dictionary program to create a dictionary in the form of (n^3) i.e. if key=2 value=8
#Input: n=4
#Output ={1 : 1, 2 : 8, 3 : 27, 4 : 64}
print("_"*50)
n = 6
output = {}
for i in range(1, n+1):
    output[i] = i**3

print("output :", output)