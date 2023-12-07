"""
num1 = 1234321
temp = num1
rev = 0
while num1 > 0:
    last_num = num1%10
    print("last_num:", last_num)
    rev  = rev*10 + last_num
    print("reverse :", rev)
    num1 = num1//10
    print("num1 :", num1)
    print("_"*40)
if temp == rev:
    print("The given number is palindrome :", temp)
else:
    print("The given number is not palindrome :", temp)
"""

#
# print("_"*40)
# last_num = num1%10
# print("last_num:", last_num)
# rev  = rev*10 + last_num
# print("reverse :", rev)
# num1 = num1//10
# print("num1 :", num1)
#
# print("_"*40)
# last_num = num1%10
# print("last_num:", last_num)
# rev  = rev*10 + last_num
# print("reverse :", rev)
# num1 = num1//10
# print("num1 :", num1)
#
# print("_"*40)
# last_num = num1%10
# print("last_num:", last_num)
# rev  = rev*10 + last_num
# print("reverse :", rev)
# num1 = num1//10
# print("num1 :", num1)

# 10). Python for loop program to print the alphabet pattern ‘O’ using python.
# Output:
"""
  * * *  
*       *
*       *
*       *
*       *
*       *
  * * * 
"""
# first block

"""

for i in range(5):
    if i == 0 or i == 4:
        print(" ", end=" ")
    else:
        print("*", end=" ")
print()

# block 2
for j in range(5):
    for i in range(5):
        if i == 0 or i == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# block 3:
for i in range(5):
    if i == 0 or i == 4:
        print(" ", end=" ")
    else:
        print("*", end=" ")
print()
"""


pattern = "*"

for j in range(2):
    for i in range(20):
        if i in [3, 4, 5, 6, 7]:
            print(" ", end=" ")
        else:
            print(pattern, end=" ")
    print()

for i in range(3):
    for j in range(15):
        if i == 1:
            if j in [3, 4, 6, 7, 11, 12, 14]:
                print(" ", end=" ")
            else:
                print(pattern, end=" ")
        else:
            if j in [3, 4, 5, 6, 7, 11, 12, 13, 14]:
                print(" ", end=" ")
            else:
                print(pattern, end=" ")
    print()

for j in range(2):
    for i in range(20):
            print(pattern, end=" ")
    print()

for i in range(3):
    for j in range(20):
        if i == 1:
            if j in [5, 8, 9, 10, 14, 17, 18, 19]:
                print(pattern, end=" ")
            else:
                print(" ", end=" ")
        else:
            if j in [8, 9, 10, 17, 18, 19]:
                print(pattern, end=" ")
            else:
                print(" ", end=" ")
    print()

for i in range(2):
    for j in range(20):
        if j in [11, 12, 13, 14, 15, 16]:
            print(" ", end=" ")
        else:
            print(pattern, end=" ")
    print()

"""
* * *           * * * * * * * * * * * * 
* * *           * * * * * * * * * * * * 
* * *           * * *         
* * *     *     * * *     *   
* * *           * * *         
* * * * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * * 
                * * *             * * * 
          *     * * *       *     * * * 
                * * *             * * * 
* * * * * * * * * * *             * * * 
* * * * * * * * * * *             * * * 




"""