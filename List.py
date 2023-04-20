# # x=[1,2,3]
# # a,b,c=x
# # print(a)
# # print(a,b,c)
# #
# # y=a,b,c
# # print(y[1])
# #
# # department = (“math", “Biology", “Computer", “chemistry")
# # department[0] = “Medicine“
# # TypeError: 'tuple' object does not support item assignment
#
#
#
# #
# # using zip function
# # 1. >>> x = [1, 2, 3]
# # 2. >>> y = [4, 5, 6]
# # 3. >>> zipped = zip(x, y)
# # 4. >>> list(zipped)
# # [(1, 4), (2, 5), (3, 6)]
# print(zipped)
#
# #
# # when you are using zip, same size
#
#
#
#
# # >>> fish = {"g": "goldfish", "s":"shark", "n": "needlefish"}
# # >>> fish
# # {'g': 'goldfish', 's': 'shark', 'n': 'needlefish}
# # >>> type(fish)
# # <class 'dict’>
# # >>> empty_dictionary = {} # creates empty dictionary
#
#
# passwd = {"guido":"superprogrammer", "turing":"genius","bill":"monopoly“}
# print(passwd["guido"])
#
# passwd["bill"] = "bluescreen“ #Dictionaries are mutable.
# {'guido': 'superprogrammer', 'bill': 'bluescreen', 'turing':'genius'}
#

passwd = {"guido":"superprogrammer", "turing":"genius","bill":"monopoly“}
list(passwd.keys())
list(passwd.values)
"bill" in passwd

print(passwd.get('fred','unknonw'))