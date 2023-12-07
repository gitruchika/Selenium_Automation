"""
def function_name(parameter):
    code
"""

def addition_value(num1, num2):
    print("add value :", num1 + num2)


# Pass by values
addition_value(50, 60)
addition_value(100, 600)

# Pass by reference
x = 900
y = 700
addition_value(x, y)

# parameter missing value
# addition_value(60)
# TypeError: addition_value() missing 1 required positional argument: 'num2'


list1 = [5, 8, 23, 11]

print(max(list1))
print(max([4, 7, 8, 1]))

def get_square_values(l1):
    output = [x**2 for x in l1]
    print(output)


get_square_values([5, 7, 1, 8, 12]) # pass by values
list1 = [4, 8, 234, 23, 13]
get_square_values(list1) # pass by reference


# default value to the parameter
# if any parameter has default value, then it will come in right most side.
def function2(num1, num2, num3=500):
    print("num1:", num1)
    print("num2:", num2)
    print("num3:", num3)
    x = num1 + num2
    y = x + num3
    print("addition value :", y)

function2(40, 60) # addition value : 600
function2(70, 20, 17) # addition value : 134
var = function2(num3=50, num2=80, num1=90) # addition value : 220
print("var :", var)


print("_"*50)
# function return type
def addition_data(var1, var2):
    return var1 + var2

result = addition_data(50, 70)
print("result :", result)

print("_"*50)
# *args function parameters.

def get_sum_values(*temp):
    print(temp)
    sum_value = 0
    for val in temp:
        sum_value += val
    print("sum of values :", sum_value)

    # for val in temp:
    #     print(val)



get_sum_values(4, 7, 2, 8)
#get_sum_values(4, 7, 2, 8, 55, 66, 22, 44, 55, 'Hello', [3, 5, 7, 2], 'Python')

#### Function with **kwargs ####


# def get_user_details(**kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(key, ":", value)

def get_user_details(**p):
    print(p)
    for key, value in p.items():
        print(key, ":", value)

get_user_details(name='john', email='john@gmail.com', phone_number = 234555344, address ='Mumbai')



##### function documentation #####
print("_"*50)
def user_details(city, mobile, *args, **kwargs):
    """
    This function help to get the users details
    :param city:
    :param mobile:
    :param args:
    :param kwargs:
    :return:
    """
    print("City :", city)
    print("Mobile :", mobile)
    print("list of inputs :", args)
    print("key value pair of the data :", kwargs)

user_details('Bangalore', 898898574985, 4, 6, 7, 23, 22, name='Rahul', age=23, phone=98989956554)

# get function document
print(user_details.__doc__)


# write a function for login functionality
print("_"*50)
def login(**kwargs):
    db_username = 'admin'
    db_password = 'admin@123'

    if kwargs['username'] == db_username and kwargs['password'] == db_password:
        print("Login Successful")
    else:
        print("Access denied, enter correct username password")

#login(username='user1', password='user@123')
#login(username='admin', password='admin@123')

# Write a Python function program to get reverse all the words in the string
str1 = "Hello Good Morning"
output= "olleH dooG gninroM"



####### declare function with DataType #########


def find_out_the_greatest(num1: int, num2: int, num3:int):
    """
    :param num1: First number to validate
    :param num2: Second number to validate
    :param num3: Third number to validate
    :return:
    """
    if num1 > num2 and num1 > num3:
        return f"Num1 has greater value : {num1}"
    elif num2 > num1 and num2 > num3:
        return f"Num2 has greater value : {num2}"
    elif num3 > num1 and num3 > num1:
        return f"Num3 has greater value : {num3}"

result = find_out_the_greatest(50, 60, 70)
print(result)

result2 = find_out_the_greatest('Hello', 'Good', 'Morning')
print(result2)



















