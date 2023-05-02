


# alphabet=list(string.ascii_lowercase)
# print(alphabet)
#
# i=1
# alpha_dic={}
# for l in alphabet:
#     alpha_dic[l]=i
#     i=i+1
#
# print(alpha_dic)




#execption example



x=input("Enter value for x: ")
y=input("Enter value for y: ")
try:
    result=int(x)/int(y)
except ZeroDivisionError:
    print("Division by zero!")
except ValueError:
    print("Please enter a number!")
else:
    print(f"Result is {result}")
finally:
    print("Executing finally clause")


# Example 3:

total=0
count=0
while True:
    num = input("Enter a number: ")
    if num == 'done':
        print(f"Sum = {total}")
        print(f"Count = {count}")
        print(f"Average = {total/count}")
        break
    else:
        try:
            total += float(num)
        except:
            print("Invalid input")
            continue
        count+=1









