# fruits = ["grapefruit", "pineapple", "blueberries", "mango", "banana"]
# fruits[-2:-5]
#
#
# fruits[0]
# fruits [2]
# fruits [-3]
# fruits [9]

# IndexError: list index out of range
# fruits[1:3]
# ['pineapple', 'blueberries’]
# fruits[:3]
# ['grapefruit', 'pineapple', 'blueberries’]
# fruits[2:]
# ['blueberries', 'mango', 'banana’]
# fruits[1:4:2]
# ['pineapple', 'mango’]
# fruits[-2:-5]
# ['grapefruit', 'pineapple', 'blueberries', 'mango', 'banana’]
# fruits[::2]
# ['grapefruit', 'blueberries', 'banana’]
# fruits[::-1]
# ['banana', 'mango', 'blueberries', 'pineapple', 'grapefruit']
#
#
#
# Python Nested List
# nested_list = [[1] ,[17, 19], [21,23,25],
# [32,35,37,39]]
# # >>> nested_list[2]
# # [21, 23, 25]
# # >>> nested_list[2][1]
# # 23
# # >>> nested_list[2][1:3]
# # [23, 25]
# # >>> nested_list[1:4]
# # [[17, 19], [21, 23, 25], [32, 35, 37, 39]]
# # >>> nested_list[1:4][1:3]
# # [[21, 23, 25], [32, 35, 37, 39]]
# # >>> nested_list[1:4][-1][1:3]
# # [35, 37]
#
#
# # A = [[1], [17,19], [21,23,25], [32,35[37,[39]]]]
# # # print(A[3][2])
# # # print(A[3][2][0])
# # # print(A[3][2][0])
# #
# #
# # numbers=[1,2,3,4,5]
# # print(sum(numbers))
# # print(max(numbers))
# # print(min(numbers))
# # x = any([1, 1, 0, 0, 1, 0])
# # print((x))
# #
# # print(all([1, 1, 1, 1])
#
# # names = ['Kim', ' lee', 'Dave', 'Bob']
# # print(sorted(names))
# # print(names)
#
#
# # names = [10, 300, 200, 5]
# # print(sorted(names,reverse=True))
# # print(names)
#
#
# cities = ["oslo", "delhi", "washington", "london",
# "seattle", "paris", "washington"]
# cities.count('seattle’)
# cities.index('washington’)
# cities.reverse()
# cities
# ['washington', 'paris', 'seattle', 'london', 'washington',
# 'delhi', 'oslo']
# cities.append('brussels')
# cities
# ['washington', 'paris', 'seattle', 'london', 'washington',
# 'delhi', 'oslo', 'brussels']
# cities.sort()
# cities
# ['brussels', 'delhi', 'london', 'oslo', 'paris’, 'seattle', 'washington', 'washington']
# cities.pop()
# 'Washington’
# cities
# ['brussels', 'delhi', 'london', 'oslo', 'paris',
# 'seattle', 'washington']
# more_cities = ["brussels", "copenhagen"]
# cities.extend(more_cities)
# cities
# ['brussels', 'delhi', 'london', 'oslo', 'paris',
# 'seattle', 'washington', 'brussels', 'copenhagen']
# cities.remove("brussels")
# cities
# ['delhi', 'london', 'oslo', 'paris', 'seattle',
# 'washington', 'brussels', 'copenhagen'
#
# print(sorted(cities))
# cities.sort()
# x=sorted(cities)
# print(x)
# print(cities)
# print((cities))
#
#
# more_cities=["brussels","copenhagen"]
# cities.extended(more_cities)


a=[5,-8,99.99,432,108,213
print(del a[0])


cars= ("ferrari", “Toyota", "mercedes", “KIA", "renault“)
>>> type(cars)
<class 'tuple’>
>>> empty_tuple = ()
>>> tuple_1 = (2, 0, 1, 4)
>>> tuple_2 = (2, 0, 1, 9)
>>> tuple_1 + tuple_2
(2, 0, 1, 4, 2, 0, 1, 9)
>>> tuple_1 * 3
(2, 0, 1, 4, 2, 0, 1, 4, 2, 0, 1, 4)
>>> tuple_1 == tuple_2
False
>>> tuple_items = (1, 9, 8, 8)
>>> 25 in tuple_items
False
>>> letters = ("a", "b", "c")
>>> numbers = (1, 2, 3)
>>> nested_tuples = (letters, numbers)
(('a', 'b', 'c'), (1, 2, 3))


a=[1,2,3]
