
students = ['Jake', 'Erina', 'Teresa', 'Ashlee', 'jiwon', 'suyeon']
print(students[0])
print('Jake' in students)
print('Elena' in students)

for s in students:
    if len(s) == 5 or len(s)==4 or len(s) == 3:
        print(s)


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
"Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
n = int(input("Enter a month number (1-12): "))
print ("The month abbreviation is", months[n-1])


myList = [1, "Spam", 4, "User"]
print([1,2] + [3,4])
[1, 2, 3, 4]
print([1,2]*3)
[1, 2, 1, 2, 1, 2]

grades = ['A', 'B', 'C', 'D', 'F']
print(grades[0])
print(grades[2:4])
print(len(grades))


list_1 = [1, 3, 5, 7, 10]
list_2 = [2, 4, 6, 8]
list_3 = [1, 3, 5, 7, 10]
list_4 = [7, 5, 3, 1]
list_1 == list_2
False
list_1 == list_3
True
list_1 == list_4
False



x=range(10)
y="UAC"
print(list(x))
print(list(y))