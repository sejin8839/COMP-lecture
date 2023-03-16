#Reverse#
S = "HELLO"
reverse_name = ' '

#1
for c in S:
    reverse_name = c + reverse_name

print(f'name    : {S}')
print(f'reverse : {reverse_name}')

#2
print(S[::-1])


# f(x) = 1/x^2#
x= int(input('Enter x: '))
if x==0:
    print('error- div by 0')
else:
    print(f'f(x) = {1/(x**2)}')


#Boolean#
s= [-100, 200, 300]
print(bool(s))


#for Loop#

# for VAR in ITERABLE:
#  BLOCK

# ITERABLE MEAN = SEQUENCE

#range()function creates a sequence or a series of numbers(integers)
#Syntax: range(start, stop, step)

x = range(6)
print(x)

print(list(x))

print(list(range(3,6)))

print(list(range(3,10,2)))


# 세로로 출력
for i in range(10):
    print(f"{i}")

# 가로로 출력
for i in range(10):
    print(f"{i}", end=" ")

# 제곱 출력
for i in range(10):
    print(f"{i**2}", end=" ")

#헤헤
S =  "Hello"
for i in s:
    print(i, end="")



#EXAMPLE 1#
# What does if I 2 == 0 mean in Python?
# if not i%2==0 can also be written as, if (i%2!=0).
# i%2 gives the remainder obtained when i is divided by 2.
# So the expression stands true if the remainder of i when divided by 2 is not 0.
# Therefore, the expression stands true for all odd numbers because any odd number when divides with 2,
# leaves a remainder of 1#

number= int(input('Enter the number: '))
sum_even = 0
sum_odd = 0
for i in range(number):
    if i % 2 == 0:
        sum_even = sum_even + i
    else:
        sum_odd = sum_odd + i
print(f"Sum of Even numbers are {sum_even} and Odd numbers are {sum_odd}")


#While#
a = 10
while a < 40:
    print(a)
    a=a+1
    a=a+3

#
number = int(input("Enter a number up to which you want to find the average: "))
i = 0
summ = 0
count = 0
while i < number:
    i = i+1
    summ = summ + i
    count = count + 1
average = summ/count + 1
print(f"The average of {number} natural number is {average}")


#write Python Program to find the sum of digits in a Number
A = int(input('Enter a number:'))
result = 0
remainder = 0
while number != 0:
    remainder = number % 10
    result = result + remainder
    A = int(A/10)
print(f"The sum of all digits is {result}")



#program to Demonstrate break Statement
n = 0
while True:
    print(f"The latest value of n is {n}")
    n = n + 1
    if n > 5:
        print(f"The value of n is greater than 5")
        break

#program to Demonstrate continue Statement
var = 10
while var > 0:
    var = var =1
    if var == 5:
        print(f'breaking at:{var}')
        continue
    print(f'Current variable value:{var}')

