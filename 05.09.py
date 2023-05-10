
myfile = open("Example.txt", mode='r')

for i in myfile:
    print(i)


# myfile =open("C:/comp1010/Example.txt",mode='r')
# for i in myfile:
#     print(i)


lst =[i*2 for i in range(1,10)]
myfile = open("Example.txt", mode='w')


inputFile = open("Example.txt", "r")
for each_line in inputFile:
    print(each_line)

inputFile.close()
print(f"File Name is {inputFile.name}")
print(f"File state is {inputFile.closed}")
print(f"File Opening mode is is {inputFile.mode}")




try:
    f=open("Example.txt","r")
    for each_line in f:
        print(each_line,end='')
except IOError:
    print('file does not exist')
finally:
    f.close()


with open("Example.txt","r") as f:
    for each_line in f:
        print(each_line,end='')


for l in lst:
    myfile.write(str(l))

