tuple1 = (3, 65, 2.4, 'hello', [3, 6, 7], {'a': 23, 'b': 34}, True, False)

print(tuple1[4]) # [3, 6, 7]
print(tuple1[4][1]) # 6

print(tuple1[3:6])
# ('hello', [3, 6, 7], {'a': 23, 'b': 34})

# methods
print(dir(tuple))
# 'count', 'index'

# count method:
tup1 = (4, 6, 9, 23, 56, 4, 6, 6)
print(tup1.count(6)) # 3

# Index method
print(tup1.index(56)) # 4

# apply loop on the tuple
print("_"*50)
tup2 = (4, 7, 23, 56, 33)
for val in tup2:
    print(val)


print("_"*50)
for i in range(len(tup2)):
    print(i, tup2[i])


# print the tuple in reverse order
tup11 = (46, 7, 8, 23, 56)
print(tup11[::-1])
# (56, 23, 8, 7, 46)

#################################################
# tup22 = (5, 7, 8, 2, 15)
#
# tup22[2:4] = (50, 100)
# print(tup22)
#TypeError: 'tuple' object does not support item assignment

# concatenate tuple values
tupa = (4, 7, 8, 2)
tupb = (13, 26, 45, 7)

tupc = tupa + tupb
print(tupc)
# (4, 7, 8, 2, 13, 26, 45, 7)

# repeat tuple values
tupn = (4, 6, 8)
tupm = tupn*5
print("tupm :", tupm)
# tupm : (4, 6, 8, 4, 6, 8, 4, 6, 8, 4, 6, 8, 4, 6, 8)

# Get max value from tuple
tupk = (4, 7, 22, 5, 66)
print("max value :", max(tupk))
print(" min value :", min(tupk))
print("Total sum of value :", sum(tupk))

print("_"*50)
list1 = [4, 7, 8, 223, 55, 10]

print("max value :", max(list1))
print(" min value :", min(list1))
print("Total sum of value :", sum(list1))