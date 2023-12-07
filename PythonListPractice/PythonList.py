list1 = [30, 50, 'Hello', [4, 7, 8], (1, 4, 6), {'a' : 123, 'b' : 345}]

print(list1[2]) # Hello

print(list1[3]) # [4, 7, 8]
print(list1[3][1]) # 7

print(list1[4][2]) #6

print(list1[2][1]) # e

print(list1[5]['a']) # 123


#  list slicing
list2 = [4, 6, 7, 2, 8, 12, 45]
print(list2[2:5])  # [7, 2, 8]

print(list2[-3:]) # [8, 12, 45]

print(list2[::2])  # [4, 7, 8, 45]

print(list2[-2:-6:-1]) # [12, 2]

print(list2[-1:-8:-1]) # [45, 12, 8, 2, 7, 6, 4]

# reverse the list with slicing
print(list2[::-1]) # [45, 12, 8, 2, 7, 6, 4]

# apply loop on the list
print("_"*50)
# without indexing
list3 = [4, 7, 8, 23, 6, 8, 2]
for val in list3:
    print(val, end=" ")
# 4 7 8 23 6 8 2

# Without indexing
print()
for i in range(len(list3)):
    print(i, list3[i])


### Program to print the even numbers from given list ####
print("_"*50)
list4 = [5, 7, 9, 2, 34, 12, 43]
for val in list4:
    if val%2 == 0:
        print(val)
    else:
        continue

####### List Methods #######
print(dir(list))
"""
'append', 'clear', 'copy', 'count', 'extend',
 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""

#### Add data to the list #####
# Append method : This method will add content at the end of the list.
lista =[5, 7, 9, 12]
lista.append(50)
print("lista :", lista)
# [5, 7, 9, 12, 50]

# Insert Method: This method add data at specific index
listb = [3, 6, 8, 12, 23]
listb.insert(2, 100)
print("listb :", listb)
# [3, 6, 100, 8, 12, 23]

# Extend method : This method extend one list with another list members.
listp = [3, 6, 7, 23, 22]
listq = ['a', 'b', 'c', 'd']

#listp.append(listq)
#print(listp)
# [3, 6, 7, 23, 22, ['a', 'b', 'c', 'd']]

# listp.extend(listq)
# print("listp :", listp )
# [3, 6, 7, 23, 22, 'a', 'b', 'c', 'd']

# list concatenation:
listm = [3, 6, 8, 9]
listn = ['p', 'q', 'r', 's']
listr = listm + listn
print(listr)
# [3, 6, 8, 9, 'p', 'q', 'r', 's']

############## Remove Data from the list ###############
list11 = [5, 7, 8, 23, 12, 33, 23]

# Remove method : We have remove any member from the list with value
list11.remove(23)
print("list11:", list11)
# list11: [5, 7, 8, 12, 33, 23]
list11.remove(23)
print("list11:", list11)
# list11: [5, 7, 8, 12, 33]

# pop method :This method remove the data from list using index position.
list12 = [5, 7, 8, 23, 12, 33, 23]
val = list12.pop() # by default index will be -1
print("value :", val)
print("list12 :", list12)

val2 = list12.pop(4)
print("value:", val2)
print("list12 :", list12)


# del function to remove data from list
list55 = [4, 6, 7, 8]
del list55 # this will remove entire list from the memory
# print(list55)


# partially remove the some values from the list
list66 = [5, 7, 3, 5, 23, 45, 12]
del list66[2:6]
print(list66) # [5, 7, 12]

del list66[1]
print(list66) # [5, 12]

# clear method: this method remove all the data from list
list77 = [4, 7, 9, 23, 56]
list77.clear()
print("list77 :", list77)
# list77 : []

list77.append(90)
print("list77 :", list77)

########### Replace the data from the list ########

listr = [5, 7, 8, 23, 67]
listr[1:4] = ['a', 'b', 'c']
print("listr :", listr)
# listr : [5, 'a', 'b', 'c', 67]

####### Repeat the list data ################
listy = [5, 7, 8, 9]
listz = listy*5
print(listz)
# [5, 7, 8, 9, 5, 7, 8, 9, 5, 7, 8, 9, 5, 7, 8, 9, 5, 7, 8, 9]


###### sort the list data #######

#### sort method :
listd = [4, 6, 7, 12, 1, 5]

# sort the ascending order
# listd.sort()
# print(listd)
# [1, 4, 5, 6, 7, 12]

# sort the data in descending order
listd.sort(reverse=True)
print(listd)
# [12, 7, 6, 5, 4, 1]


### sorted function ###
listg = [4, 6, 8, 2, 1, 5]
result = sorted(listg)
print("sorted result :",result )
#[1, 2, 4, 5, 6, 8]
print("listg :", listg)
# listg : [4, 6, 8, 2, 1, 5]


# descending order
result2 = sorted(listg, reverse=True)
print("descending result :", result2)
# [8, 6, 5, 4, 2, 1]

print("listg :", listg)
# listg : [4, 6, 8, 2, 1, 5]


####### Reverse Method ######
print("_"*50)
listh = [4, 7, 2, 3, 5, 12]

# reverse method : This method reverse the content of the list and modify the input list
#                  in place
listh.reverse()
print("listh :", listh)


# reversed function : This function return the reverse value of the list through object.
listj = [4, 6, 1, 7, 34]

input_data = reversed(listj)
print(input_data)
for val in input_data:
    print(val, end=" ")
# <list_reverseiterator object at 0x0000011B69B338B0>
# 34 7 1 6 4

# count method : This method count repeatation of any value in the list
print("_"*50)
listk = [4, 6, 8, 4, 6, 2, 4, 2]
print("count of 4:", listk.count(4))

print("_"*50)
#### copy method ####
# shallow copy
listv = [4, 7, 9, 2, 5]
listm = listv
listm.append(20)
listn = listm
listn.append(100)

print("listv :", listv)
print("listm :", listm)
print("listn :", listn)

# Deep Copy
listx = [33, 55, 23, 21, 45]
listy = listx.copy()
listy.append(50)

print("list x:", listx)
print("list y:", listy)
# list x: [33, 55, 23, 21, 45]
# list y: [33, 55, 23, 21, 45, 50]


# Index method: This method return the index of any specific value in the list.
listg = [5, 7, 23, 22, 14, 66]
print(listg.index(14)) # 4
print(listg.index(23)) # 2


# Programs: get square all the values in the list
print("_"*50)
list1 = [3, 6, 7, 12, 23]
list2 = [] # [9, 36, 49, 144, 529]
for i in range(len(list1)):
    print(list1[i]**2)
    var = list1[i]**2
    list2.append(var)

print(list2)


# Program : get all the values from list which are divisible by 3 and add to another list
listu = [5, 7, 9, 21, 15, 44, 33]
output = []
for i in range(len(listu)):
    var = listu[i]
    if var%3 == 0:
        output.append(var)
    else:
        continue

print("output :", output)
# output : [9, 21, 15, 33]


# program: add all even and odd number in two separate list from given data
listo = [4, 6, 3, 45, 22, 33, 31, 24, 65]
list_even = []
list_odd = []

for i in range(len(listo)):
    var1 = listo[i]
    if var1%2 == 0:
        list_even.append(var1)
    else:
        list_odd.append(var1)

print(list_even)
print(list_odd)

##### List Comprehension ######
print("_"*50)
list1 = [5, 7, 9, 2, 6, 12]
# square of all the values
result = [val**2 for val in list1]
print("result :", result)

# get all the even values from the list
result2 = [val for val in list1 if val%2 == 0]
print("result 2:", result2)

# output = [(5, "odd"), (7, "odd"), (9, "odd"), (2, "even"), (6, "even")]

result3 = [(val, "even") if val%2 ==0 else (val, "odd") for val in list1]
print("result3 :", result3)

######################################################################################
# program : find out the common element from the given lists
list1 = [3, 5, 7, 2, 8, 1]
list2 = [1, 6, 9, 3, 5, 2]
common_values = []

for val in list1:
    if val in list2:
        common_values.append(val)
    else:
        continue

print("common values :", common_values)
# common values : [3, 5, 2, 1]

result = [val for val in list1 if val in list2]
print("result :", result)
# result : [3, 5, 2, 1]

############################################
# write a python program to print below output
str1 = "Hello Good Morning, Hope You are doing good"
#output = ['H', 'G', 'M', 'H', 'Y', 'a', 'd', 'g']
output = []

word_list = str1.split()
for word in word_list:
    first_char = word[0]*2
    last_char = word[-1]*2
    middle_char = word[1:-1]
    new_word = f"{first_char}{middle_char}{last_char}"
    output.append(new_word)

print(output)



# write a python program to print the output
str1 = "Hello Good Morning Hope You are doing good"
output = ["HHelloo", "GGoodd", "MMorningg", "HHopee", "YYouu", "aaree", "ddoingg", "ggoodd"]














