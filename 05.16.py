import os
print(os.getcwd())
print(os.listdir())
print(os.rename("Employee.txt", "workers.txt"))
#os.remove("example1.txt")
# os.mkdir("Data_Science")
os.chdir("COMP-lecture")
print(os.getcwd())
print(os.listdir())
print(os.walk(os.getcwd()))
for dirpath,dirnames,filenames in os.walk(os.getcwd()):
print('path:',dirpath)
print('Dirs:',dirnames)
print('fileNames:',filenames)
print()