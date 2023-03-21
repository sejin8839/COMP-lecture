
n = int(input('Enter the value of n: '))
sum = 0
num=0
while num< n:
    sum = sum + num
    num+=1
    print(f"SUM = {sum}")
print(f"SUM = {sum}")

# ^ tab 하느냐 안 하느냐 차이 중요 하다는 거 확인 하기

nums = input('Enter numbers, space separated:')
sum1 = 0
numbers = nums.split()
for n in numbers:
    sum1 = sum1 + int(n)
print(f"SUM = {sum1}")



rate = float(input("Enter rate: "))
hours = float(input("Enter hours worked: "))
if hours > 40:
    pay = 40 * rate + (hours - 40) * 1.5 * rate
else:
    pay = hours * rate
print(f"Pay=${pay}")

# All the same

import math
print(f'pi={math.pi}')
print(f' the square of 7 is {math.pow(7, 2)}')

import math as m
print(f'pi={m.pi}')
print(f' the square of 7 is {m.pow(7, 2)}')

from math import pi,pow
print(f'pi={pi}')
print(f' the square of 7 is {pow(7, 2)}')
