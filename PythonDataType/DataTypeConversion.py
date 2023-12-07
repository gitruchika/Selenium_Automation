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
print("_"*50)
num2 = 678
list1 = list(num2)
print(list1)
"""
# int -> tuple # conversion is not possible
# int -> dict # conversion is not possible
# int -> set # conversion is not possible
# int -> boolean
num3 = -1
var1 = bool(num3)
print(var1) # False

num4 = 23
var2 = bool(num4)
print(var2) # True

######## Float ########

