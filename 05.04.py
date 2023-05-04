def bubble_sort(numbers):
    for  i in range(len(numbers)-1):
        for j in range(len(numbers)-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

N = [4,3,12,1,5,17,12,2,6,9,10]
print(bubble_sort(N))


a=6
print(type(a))

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary


e1=Employee("David",6000)
e2=Employee("Helen",8000)

print(type(e1))
print(e1.name)
print(e2.name)
print(e1.__dict__)
print(e2.__dict__)



