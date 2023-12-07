a = 5
# = : Assignment operator
# a : variable
# 5 : value to assign
print(id(a)) # It provides the address location
print(a)

b = 'Good Morning'
print(id(b))

c = 10

# addition of values
d = a + c
print(d, id(d))

# Check the type data
p = 50
q = 'Hello World'
r = 55.45
print("Type of p ->", type(p))
print("Type of q ->", type(q))
print("Type of r ->", type(r))

#Rules to declare variable
#1. There should not space in the variable name.
# a b c = 50  # wrong name
# SyntaxError: invalid syntax
abc = 50  # correct name
a_b_c = 60 # correct name

print(a_b_c)
print(abc)

# 2. We can not start the variable name with number
# 1city = 'Mumbai' # #wrong name
city1 = 'Mumbai'
city_13456 = 'Kolkata'
print(city1, city_13456)

#3 Variable name are case sensitive.
Name = 'John'
NAME = 'Jenny'
name = 'Dan'

print(Name, "|",  NAME, "|",  name)


# different variables with same values store at memory

var1 = 600
var2 = 600
var3 = 600

print("var1 address :", id(var1))
print("var2 address :", id(var2))
print("var3 address :", id(var3))

# multi line comment
"""
var1 address : 2294047030320
var2 address : 2294047030320
var3 address : 2294047030320
"""

# Assign a single value to multiple variable

a = b = c = 700
print("value of a", a, id(a))
print("value of b", b, id(b))
print("value of c", c, id(c))

# Assign different values to different variables at a time.
x, y, z = 60, 70, 80

print("value of x", x, id(x))
print("value of y", y, id(y))
print("value of z", z, id(z))

# Mathemetical operator
"""
+ : addition operator
- : subtraction operator
* : multiplication operator
/ : division operator 
// : division operator
** : power operator
"""
# addition of the number
a1 = 60
b1 = 80
print("addition :", a1 + b1)
print("subtraction :", a1 - b1)
print("multiplication :", a1 * b1)

p1 = 15
q1 = 2
# division with single /
r1 = p1/q1
print("value of r1:", r1, type(r1))
# value of r1: 7.5 <class 'float'>

# division with double //
t1 = p1//q1
print("value of t1:", t1, type(t1))
# value of t1: 7 <class 'int'>

# show power of any value
num1 = 5
print("square of 5 :", num1**2)
print("cube of 5 :", num1**3)

# Solve given equation

#(a+b)^2  = a^2 + b^2 + 2ab
a = 8
b = 7
# LHS
lsh = (a+b)**2
print("LSH output:", lsh)

# RHS
rhs = a**2 + b**2 + 2*a*b
#      64 + 49 + 2*7*8
print("RHS output :", rhs)

######################################
import math
# c^2 = a^2 + b^2
a = 4
b = 5

rhs = a**2 + b**2
print("rhs :", rhs)

#c**2 = 41
print(math.sqrt(rhs))
# value of c : 6.4031242374328485
