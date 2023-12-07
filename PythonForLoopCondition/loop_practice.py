# write a program to print numbers
for i in range(10):
    print(i)

# i : variable name
# range() : initial value, last value, difference of values
# range(10) :
# initial value is zero,
# last value will be 10
# difference of values in 1
print("_"*50)
for i in range(2, 21, 2):
    print(i)

print("_"*50)
string1 = "Python Programming"
for char in string1:
    print(char)

# print numbers in reverse order
print("_"*50)
for i in range(10, 0, -1):
    print(i)


# get the even numbers from given list values
print("_"*50)
lista = [4, 7, 23, 44, 55, 12]
for val in lista:  # val = 4, 7, 23, 44, 55, 12
    #print(val)
    if val%2 == 0: # val%2 == 0, 4%2 ==0, 7%2 == 0, 23%2 ==0, 44%2 ==0, 55%2 === 0, 12%2 ==0
        print(val) # 4, 44, 12

## check given number is prime number or not.
"""
print("_"*50)
user_input = int(input("Please enter value:"))
prime = True
for i in range(2, user_input):
    if user_input%i == 0:
        prime = False

if prime:
    print("This is prime number :", user_input)
else:
    print("This is not prime number :", user_input)

"""
########## Nested for loop condition #######
print("_"*50)
for i in range(5):
    for j in range(3):
        print("address :", i, "package :", j)

    print("_"*50)


###### Get of prime number between 1 to 50 ####

for num in range(1, 51):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False

    if prime:
        print("This is prime number :", num)
    # else:
    #     print("This is not prime number :", num)



################# While Loop ########
"""
print("_"*50)
num1 = 1
while num1 <= 10:
    print(num1)
    num1 = num1 + 1


# print table of any given number
print("_"*50)
temp = 1
N = int(input("Enter the number :"))
while temp <= 10: # 1 <= 10| 2 < 10
    print(temp, "*", N, ":", temp*N)
    #  1 * 5 : 5
    # 2 * 5 : 10
    temp = temp + 1 # 2, 3


# run infinite loop
while True:
    print(temp)
    temp = temp + 1
    # stop the loop with break statement
    if temp == 100001:
        break


# continue and break statement
print("_"*50)
for i in range(1, 20):
    if i == 4 or i == 7 or i == 9:
        continue
    elif i == 15:
        break
    print(i)

"""
# Write a Python program to print given pattern.
"""
*
* *
* * *
* * * *
* * *
* *
*
"""

for i in range(1, 5): #i = 1, 2, 3
    for j in range(i):# j = 0 | j = 0, 1 | j = 0, 1, 2
        #print(f"* i:{i}, j:{j}", end=" ")
        print("*", end=" ")
    print()

for k in range(3, 0, -1):
    for l in range(k):
        print("*", end=' ')
    print()


# print number pattern
"""



"""
temp = 1
for i in range(1, 5):
    for j in range(i):
        print(temp, end="   ")
        temp = temp +1
    print()

for k in range(3, 0, -1):
    for l in range(k):
        print(temp, end='   ')
        temp = temp + 1
    print()


# ACSCII 65-90 Capital letter
print(chr(65))

# ASCII 97 - 122 small letter
print(chr(97))


temp = 65
for i in range(1, 5):
    for j in range(i):
        print(chr(temp), end=" ")
        temp = temp +1
    print()

for k in range(3, 0, -1):
    for l in range(k):
        print(chr(temp), end=' ')
        temp = temp + 1
    print()

"""
A 
B C 
D E F 
G H I J 
K L M 
N O 
P 
"""