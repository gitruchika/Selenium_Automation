set1 = {4, 6, 2, 7, 4, 6, 'a', 'b'}
print(set1, type(set1))
# {2, 4, 6, 7, 'b', 'a'} <class 'set'>
"""
-> Set only store unique data , it does not allow duplicate values.
-> Only immutable data type can member of the set, int, float, string, tuple, Boolean
-> Set is a mutable data type, we can modify any point of time.
-> Set does not follow any indexing, store data in un-structure form.
"""

set2 = {4.6, 'Hello', (4, 7, 9), True}
print(set2)

# set3 = {4.6, 'Hello', (4, 7, 9), True, [4, 8, 3]}
# print(set3)
# TypeError: unhashable type: 'list'

# set with dict
# set4 = {5.5, 'Python', 'Hello', {'a': 123, 'b' : 567}}
# print(set4)
# unhashable type: 'dict'

# Apply loop on the set
print("_"*50)
seta = {5, 8, 2, 9, 12, 3}

for val in seta: # val = 5, 8
    #print(val)
    if val%2 == 0: # 5%2 == 0 | 8%2 == 0 | 2%2 == 0 | 9%2 == 0
        print(val) # 8, 2, 12
    else:
        continue

# remove all the duplicate from list
print("_"*50)
list1 = [3, 7, 2, 8, 1, 2, 54, 7, 2, 3, 1]

set1 = set(list1)
print(set1)
list2 = list(set1)
print(list2)

print(list(set(list1)))
# [1, 2, 3, 7, 8, 54]

##### set methods ########
print("_"*50)
print(dir(set))

# 'add', 'clear', 'copy', 'difference', 'difference_update',
# 'discard', 'intersection', 'intersection_update', 'isdisjoint',
# 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
# 'symmetric_difference_update', 'union', 'update'

## add method

set11 = {5, 7, 1, 8, 'a', 'Python'}
set11.add(100)
print("set11 :", set11)
# {'a', 1, 'Python', 100, 5, 7, 8}

# union method : this method helps to combine 2 sets
setx = {4, 6, 8, 'a', 'b'}
sety = {1, 3, 2, 'Python', 'Programming'}

setz = setx.union(sety)
print("setz :", setz)
print("setx :", setx)
print("sety :", sety)
"""
setz : {1, 2, 3, 4, 6, 8, 'a', 'b', 'Python', 'Programming'}
setx : {4, 'b', 6, 8, 'a'}
sety : {1, 2, 3, 'Python', 'Programming'}
"""

# update method : this method modify the existing set values
print("_"*50)
setp = {3, 6, 9, 10}
setq = {'a', 'b', 'c'}

setp.update(setq)

print("setp: ", setp)
print("setq: ", setq)

"""
setp:  {3, 'a', 6, 'b', 9, 10, 'c'}
setq:  {'c', 'a', 'b'}
"""

"""
write a python method/function to find how many times character "me" in the list of string
["Hammer Time", "Swimmer"]
"""
str_list = ["Hammer Time", "Swimmer"]
me_count = 0
for word in str_list:
    temp = word.count("me")
    me_count = me_count + temp

print("Total me count :", me_count)

print("_"*50)
#### Remove data from set ####
# remove method:

setb = {4, 7, 8, 2, 5, 9}
setb.remove(8)

print("setb :", setb)
# setb.remove(10)# if specified data is not available in the set
# then it will through key error.
# print("setb :", setb)
# KeyError: 10

# discard method: this method also help remove data from set
setj = {7, 6, 8, 1, 4, 5}
setj.discard(4)
print("setj :", setj)

setj.discard(9) # if we remove any data which is not available in the set,
# then it will not show any error.
print("setj :", setj)

# pop method: pop method remove any random data from set and return it
# so we can store in the variable
setk = {5, 7, 23, 34, 12, 'a', 'b'}
var = setk.pop()
print("setk :", setk, var)

# clear data from set
setl = {'a', 'b', 'c', 'd'}
setl.clear()

print("setl :", setl) # set()

# delete complete set from memory
setll = {'a', 'b', 'c', 'd'}
del setll
# print("setll :", setll)
# name 'setll' is not defined. Did you mean: 'setl'?

###############################################
# intersection method : this method shows common values between two sets.

setp = {3, 6, 8, 'a', 'b', 'c'}
setq = {10, 11, 8, 'b', 'a', 'e'}

result = setp.intersection(setq)
print(result) # {'a', 8, 'b'}

# Difference between two sets.
result2 = setp.difference(setq)
print("result2 :", result2)  # {'c', 3, 6}

# superset method
setm = {5, 7, 8, 2, 15, 23, 'a', 'b'}
setn = {5, 7, 8, 23}

print(setm.issuperset(setn))# True
print(setn.issuperset(setm)) # False

print(setn.issubset(setm)) # True
print(setm.issubset(setn)) # False

#setm.difference_update(setn)
#print("setm :", setm)

# print(setm.symmetric_difference(setn))
# setm.symmetric_difference_update(setn)
# print("setm :", setm)

