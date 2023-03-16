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







