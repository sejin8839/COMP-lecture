x=[1,2,3]
a,b,c=x
print(a)
print(a,b,c)

y=a,b,c
print(y[1])

department = (“math", “Biology", “Computer", “chemistry")
department[0] = “Medicine“
TypeError: 'tuple' object does not support item assignment
