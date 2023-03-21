# conditionals
#if (True):
    #pass
    #print('hi')
#else:
    #pass

# tab is 4 space bars.
#can make multiple statements
#why the : is important?


#Loops
s=0
for x in range(1, 11):
    s=s+x
    print(s)

s=0
for x in range(1, 11):
    if(x%2==0):
        s_even=s+x
print(s_even)

# x%2==0 뜻은 x를 2로 나눴을 때 나머지가 0이면 true.


# 각 글자 세로로 하나하나 출력
s = 'Hello World'
for l in s:
    print(l)

s = 'Hello World'
i = 1
while i<len(S):
    print(s[i])
    i=i+1

# 인덱싱은 항상 0(zero)부터 시작

#while i<len(S):
    #print(s[i],end='')
    #if(s[i]==' '):
        #continue

var = 10
while var > 0:
    var = var -1
    if var == 3:
        print(f'breaking at :{var}')
        continue








