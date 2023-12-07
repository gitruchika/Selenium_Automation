result = lambda x, y : x+y

print(result(40, 20))

# map , filter reduce

list1 = [5, 7, 8, 20]
result = list(map(lambda x: x**2, list1))
print("result :", result)
# result : [25, 49, 64, 400]

list2 = [6, 7, 3, 9, 2, 24, 34, 45]

result2= list(filter(lambda x: x%2 == 0, list2))
print(result2)


# get output as single value in the city
from functools import  reduce

list3  = [6, 7, 3, 9, 2, 24, 34, 45]
reduce_result = reduce(lambda x,y : x+y, list3)

print(reduce_result)