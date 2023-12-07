# 8)  Python program to print a combination of 2 elements from the list whose sum is 10.
#          i=1
list1 = [2, 7, 3, 6, 8, 9, 1, 5, 4]
#              j=2
#output =

for i in range(len(list1)-1):
    for j in range(i+1, len(list1)):
        if (list1[i] + list1[j]) == 10:
            print(list1[i], list1[j])
        else:
            continue

"""
10). Python program to split the list into two-part, the left side all odd values and the right side all even values.
Input = [5, 7, 2, 8, 11, 12, 17, 19, 22]
Output = [5, 7, 11, 17, 19, 2, 8, 12, 22]
"""
