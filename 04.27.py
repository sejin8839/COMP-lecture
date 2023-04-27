
##
def foo():
    print("UAC")
foo()

def foo(a,b):
    print(a-b)
foo(b=2,a=3)

def foo(*a):
    print(a)
foo(3,5,6,7,8,7)

##
b=(1,3)
print(*b)

b=[1,3]
print(*b)

##
b=[1,3,5,10]
for i in b:
    print(i)

for i in b:
    print(i,end=" ")




##Examples1: Passing lists or tuples as parameter to functions
def addition1(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
result1 = addition1([1,2,3,4,5])#list
result2 = addition1([1,2,3,4,5,6,7,8])
print(result1)
print(result2)

def addition1(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
result1 = addition1([1,2,3,4,5])#list
result2 = addition1([1,2,3,4,5,6,7,8])
print(result1)
print(result2)


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


##Example: Using *args and **kwargs in Function Calls

def my_sum(a,b,c):
    print(a + b + c)
#numbers = [1,2,3]
my_sum(1,2,3)


def sum2(*args):
    result=0
    for x in args:
        result += x
    return result
list1 = [1,2,3]
list2 = [4,5]
list3 = [6,7,8,9]
print(sum2(*list1,*list2,*list3))


def sum_values(val_1,val_2,val_3):
    print("Total=", val_1+val_2+val_3)
values={"val_1":3,"val_2":10,"val_3":20}
sum_values(**values)


