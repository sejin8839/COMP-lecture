##
basket={'apple','orange','apple','pear','orange','banana'}

#1
print(type(basket))
#2
print(basket)
#3
print(len(basket))
#4
print('orange'in basket)
#5
print('crabgrass'in basket)


##
a=set('abracadabra')
b=set('alacazam')
print(a)
print(b)
print(a-b)


##
A={}
print(type(A))

B=set()
print(type(B))


##Dictionaries
dic2={"a":1,"a":2,"b":2}
print(dic2)
#remove the previous one


##
def func1(d):
    d["first"]=[1,2,3]

dic={"first":{1:1},"second":{2:"a"}}
print(dic)
func1(dic)
print(dic)

#we have to know key first value


##
dic={"first":1,"second":2,"third":3}
for i in dic:
    print(i)

dic={"first":1,"second":2,"third":3}
for i in dic:
    print(dic[i])

##
dic={"first":1,"second":2,"third":3}
print(dic)
dic["fourth"]=4
print(dic)

##
dic={"first":1,"second":2,"third":3}
print(dic)
dic["second"]=4
print(dic)


##
dic = {"first": 1, "second": 2, "third": 3}
print(dic)
dic["fourth"] = 4
print(dic)
del dic["first"]
print(dic)

##
dic = {"first": 1, "second": 2, "third": 3}
print(dic)
dic["fourth"] = 4
print(dic)
dic.pop("first")
print(dic)



##
def addition1(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
result1 = addition1([1,2,3,4,5])#list
result2 = addition1([1,2,3,4,5,6,7,8])
print(result1)
print(result2)

def addition1(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
result1 = addition1(1,2,3,4,5) #tuple
result2 = addition1(1,2,3,4,5,6,7,8)
print(result1)
print(result2)
#print(type(numbers))


def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)
multiply(4, 5)
multiply(10, 9)
multiply(2, 3, 4)
multiply(3, 5, 10, 6)
#print(type(numbers))






