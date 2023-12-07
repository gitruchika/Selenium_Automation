num1 = 20
num2 = 50

if num1 == num2:
    print("Both the numbers are equal")
else:
    print("Both numbers are not equal")

"""
conditional operators
> : greater than
< : less than
>= : greater than equal
<= : less than equal
!= : not equal
"""

"""
Logical Operator
and
True and True : True
True and False : False
False and True : False
False and False : False

or condition

True or True : True
False or True : True
True or False : True
False or False : False
"""

# check given number is even or odd.
"""
var1 = int(input("Please enter the number :"))
print(var1, type(var1))

if var1%2 == 0:
    print("This is even number")
else:
    print("This is odd number")
"""
"""
# if with multiple condition
if cond1 and cond2:
    code
else:
    code
"""

# Check given number can be divide by 3 and 5
"""
input_num = int(input("Please enter the value :"))
if input_num%3 == 0 and input_num%5 == 0:
    print("Number can divide by 3 and 5 both:", input_num)
else:
    print("The Number can not divide by 3 and 5 both:", input_num)
"""

"""
# Check given number can be divide by 3 or 7
num2 = int(input('Please enter the number :'))

if num2%3 == 0 or num2%7 == 0:
    print("The number can divide by 3 or 7:", num2)
else:
    print("The number can not divide by 3 or 7 :", num2)

"""
"""
condition with elif
if condition1:
    code
elif condition2:
    code
elif condition3:
    code
else:
    code
"""

### Program : write the a program to find the greatest number among three values
a = 70
b = 90
c = 90

if a > b and a > c:
    print("A has greater value")
elif b > a and b > c:
    print("B has greater value")
elif c > a and c > b:
    print("C has greater value")
else:
    print("No one has greater value")

# Write a Python program for calculator
"""
1. addition
2. multiplication
3. subtraction
4. division

take 2 inputs numbers from the user.
"""
print("_"*50)
print("1. addition\n"
      "2. multiplication\n"
      "3. subtraction\n"
      "4. division")
"""
var1 = int(input("Please enter choice"))
num1 = int(input("Please enter number1:"))
num2 = int(input("Please enter number2:"))

if var1 == 1:
    print("addition :", num1 + num2)
elif var1 == 2:
    print("Multiplication :", num1 + num2)
elif var1 == 3:
    print("Subtraction :", num1 - num2)
elif var1 == 4:
    print("Division :", num1//num2)


"""

########## Nested If condition #######
"""
if condition1:
    if condition2:
       code
       if condition3:
           code
       else:
           code
    else:
       code
else:
    code
"""
print("_"*50)
round1 = "fail"
round2 = "pass"
round3 = "fail"

if round1 == "pass":
    print("congrats first round is cleared")
    if round2 == "pass":
        print("congrats second round is cleared")
        if round3 == "pass":
            print("congrats, please receive offer letter")
        else:
            print("Sorry third round is not clear, please try next time")
    else:
        print("Sorry second round is not clear, please try next time")

else:
    print("Sorry first round is not clear, please try next time")


### write a python program to check the number is even and divible 3
"""
print("_"*50)
num1 = int(input("Please enter the number :"))

if num1%2 == 0:
    print("Its even number")
    if num1%3 == 0:
        print("This number can be divide by 3")
    else:
        print("Number can not divide by 3")
else:
    print("This is odd number")

"""

#### check given number is available in the list of values
print("_"*50)
list1 = [4, 7, 8, 2, 3, 5]
numa = 6
numb = 5

if numa in list1:
    print("The number is available in the list")
else:
    print("The number is not available")

if numb not in list1:
    print("Number is not in the list:", numb)
else:
    print("Number is available in the list:", numb)

# if condition in a single line
numf = 33

result = "odd" if numf%2 != 0 else "even"
print("This number is : ", result, numf)

"""
Practice Programs:
1. Write a Python Program to check given number is divide by 13 and 7
2. Write a Python Program to find the grade of student in the exam, with given marks.
# note : we have to use elif condition to solve the problems.
"""
