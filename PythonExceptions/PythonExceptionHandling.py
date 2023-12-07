
# num1 = 30
# num2 = "50"
#
# num3 = num1 + num2
# print("num3 :", num3)
#
"""
try:
    num1 = 30
    num2 = "50"

    num3 = num1 + num2
    print("num3 :", num3)
except Exception as e:
    print("Can not add int with string")
    print(e)

print("Good Morning")
"""

# raise the explicit exception
"""
try:
    num1 = 500
    num2 = 0
    result = num1//num2
except Exception as e:
    print("Can not divide by zero")
    raise
"""

"""
# try - except - else (Exception with else condition)
# else condition only executes when there is no exception in the code
try:
    num1 = 60
    num2 = 3
    division = num1//num2
    print("Division :", division)
except Exception as e:
    print("Can not divide by zero")
else:
    # Execute this code, when there is no exception
    addition = num1 + num2
    print("addition :", addition)
"""

# try - except - else - finally
# finally : this block of code executes in any condition whether there is exception in the code
# or No exception.

"""
num1 = 400
num2 = 0

try:
    division = num1//num2
    print("division :", division)
except Exception as e:
    print("Can not divide by zero")
    print(e)
# else:
#     print("addition :", num1+ num2)
finally:
    print("multiplication :", num1*num2)

"""

# customize exception msgs as per different exceptions.
"""
try:
    num1 = 70
    num2 = 50
    addition = num1 + num2
    print("addition :", addition)

    division = num1//num2
    print("division :", division)

    assert num1 == num2
except TypeError:
    print("Can not add int with string")
except ZeroDivisionError:
    print("Can not divide by zero")
except AssertionError:
    print("Both the numbers are not equal")
"""

class SQATools(Exception):
    def __init__(self):
        print("This is customize exception msg")


try :
    num1 = 60
    if num1 > 50:
        raise SQATools
except SQATools as e:
    print("Call the customize class")

