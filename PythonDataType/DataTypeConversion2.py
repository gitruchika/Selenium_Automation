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
##### Int #####
"""
# int -> float
var1 = 202
print(var1, type(var1))

var2 = float(var1)
print(var2, type(var2))
# 202 <class 'int'>
# 202.0 <class 'float'>

# int -> string
print("_"*50)
num1 = 567
svar = str(num1)
print(svar, type(svar), svar[2])

# int -> list # conversion is not possible
"""
"""
print("_"*50)
num2 = 678
list1 = list(num2)
print(list1)
"""
# int -> tuple # conversion is not possible
# int -> dict # conversion is not possible
# int -> set # conversion is not possible
# int -> boolean
"""
num3 = -1
var1 = bool(num3)
print(var1) # False

num4 = 23
var2 = bool(num4)
print(var2) # True
"""
######## Float ########

###### String #########
str1 = "Hello"

# str -> int # Can not convert into int
#num1 = int(str1)
#print(num1)
# invalid literal for int() with base 10: 'Hello'

# we can convert the string into integer when there is only numbers.
str2 = "6459085908654"
num2 = int(str2)
print(num2, type(num2), num2*2)

##### string ->  float ###
stra = '56.67'
fnum = float(stra)
print(fnum, type(fnum))


#### string -> list #####
strb = "Python"
list_output = list(strb)
print(list_output, type(list_output), list_output[1])
# ['P', 'y', 't', 'h', 'o', 'n'] <class 'list'> y

#### string -> tuple ###
tup = tuple(strb)
print(tup, type(tup), tup[0])
# ('P', 'y', 't', 'h', 'o', 'n') <class 'tuple'> P

#### string -> dict #####

"""
strc = "Programming"
dict1 = dict(strc)
print(dict1, type(dict1))
"""
# ValueError: dictionary update sequence element #0 has length 1; 2 is required
import  json
strd = '{"name" : "Rahul", "age": 25, "email": "rahul@gmail.com"}'
dict_values = json.loads(strd)
print(dict_values, type(dict_values))
print("email id:", dict_values['email'])

# string -> set : conversion is not possible
# string -> boolean
strf = ""
bool_value = bool(strf)
print(bool_value) # False


strg = "Hello"
bool_value = bool(strg)
print(bool_value) # True

############# list ##############
print("_"*50)
#1. List -> Int : conversion is not possible
#
# list1 = [4, 7, 8]
# number = int(list1)
# print(number)
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'


#2. list -> float : conversion is not possible
# list -> complex number :  conversion is not possible
# list -> string
print("_"*50)
list1 = [3, 6, 7]
str_val = str(list1) # "[3, 6, 7]"
print(str_val, type(str_val), str_val[0], str_val[1], str_val[2])

### list -> tuple ####
print("_"*50)
list2 = [3, 6, 7]
tup2 = tuple(list2)
print(tup2, type(tup2), tup2[0])

#### list -> dict ####
"""
print("_"*50)
list2 = [3, 6, 7]
dict1 = dict(list2)
print(dict1)
"""
# cannot convert dictionary update sequence element #0 to a sequence
lista = ['a', 'b', 'c']
listb = [123, 456, 789]
output = dict(zip(lista, listb))
print(output, type(output))

### list -> set #####
print("_"*50)
listc = [654,456,456,4564,564,56,456,456,45,64,56,456, 3, 8, 3]
set_var = set(listc)
print(set_var, type(set_var))
# {64, 3, 456, 8, 45, 654, 4564, 564, 56} <class 'set'>


### list -> Bool ####
list1 = []
bool_var = bool(list1)
print(bool_var)  # False

list2 = [4, 7, 8]
bool_var2 = bool(list2)
print(bool_var2) # True

###################### Tuple ###################
# tuple -> int : not possible
# tuple -> float : not possible
# tuple -> complex number : not possible
### tuple -> string ###
print("_"*50)
tup = (2, 8, 6)
str1 = str(tup) # "(2, 8, 6)"
print(str1, type(str1), str1[0], str1[1], str1[2])

### Tuple -> list ####
print("_"*50)
tup = (2, 8, 6)
list11 = list(tup)
print(list11, type(list11), list11[2])
# [2, 8, 6] <class 'list'> 6

# Tuple -> dict : not possible
# tuple -> set
tup2 = (5, 7, 5, 7, 3, 5, 7, 3, 4, 5)
set_var = set(tup2)
print(set_var, type(set_var))
# {3, 4, 5, 7} <class 'set'>

# Tuple -> Bool
# print("_"*50)
tup3 = ()
bool_var = bool(tup3)
print(bool_var, type(bool_var))  # False <class 'bool'>

tup4 = (4, 7, 9)
bool_var = bool(tup4)
print(bool_value, type(bool_var)) # True <class 'bool'>

######################## dict #######################

# dict -> int : not possible
# dict -> float : not possible
# dict -> complex : not possible
# dict -> string
print("_"*50)
dict1 = {"name": "john", "age" : 24, "salary" : 654654645}
str_var= str(dict1)
print(str_var, type(str_var), str_var[0], str_var[1], str_var[2])
# {'name': 'john', 'age': 24, 'salary': 654654645} <class 'str'> { ' n

# dict -> list
print("_"*50)
dict1 = {"name": "john", "age" : 24, "salary" : 654654645}
list1 = list(dict1)
print(list1) # ['name', 'age', 'salary']

# dict -> tuple
print("_"*50)
dict1 = {"name": "john", "age" : 24, "salary" : 654654645}
tup1 = tuple(dict1)
print(tup1) # ('name', 'age', 'salary')

# dict -> set :
print("_"*50)
dict1 = {"name": "john", "age" : 24, "salary" : 654654645}
set_var = set(dict1)
print(set_var) # {'age', 'salary', 'name'}

# dict -> bool
dict1 = {}
bool_val = bool(dict1)
print(bool_val) # False

dict2 = {"a": 123}
bool_val2 = bool(dict2)
print(bool_val2) # True







