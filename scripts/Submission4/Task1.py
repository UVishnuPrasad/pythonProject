try :
    file = open('file1.txt','r+')
    file_cont = file.read()
    print(file_cont)
except FileNotFoundError:
    print("The file is not found or  dosent exist")
