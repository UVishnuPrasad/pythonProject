file = open('file1.txt','w')
x = input("Enter text to add into the file")
if file.write(x):
    print("File contents succesfully written")

file = open('file1.txt','r')
file_cont = file.read()
print(file_cont)

file = open('file1.txt','a')
x = input("Enter text to add into the file")
if file.write(x):
    print("Contents successfully appended into the file")

file = open('file1.txt','r')
file_cont = file.read()
print(file_cont)
