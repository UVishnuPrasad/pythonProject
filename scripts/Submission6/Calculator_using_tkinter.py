#Step 1 Import
from tkinter import *
from tkinter import StringVar

#Step 2 Create GUI
calc = Tk()
calc.title("Calculator")
calc.geometry('340x180')

#Step 3 Implimentation
entry = Entry(calc,width=55)
entry.place(x=0,y=0)

def click(num):
    result = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(result)+str(num))


num1 = Button(calc,text="1",command=lambda: click(1),width=10,font="Bold",bg="Black",fg="White",activeforeground="Black",activebackground="Pale green")
num1.place(x=0,y=20)

num2 = Button(calc,text="2",command=lambda: click(2),width=10,font="Bold",bg="Black",fg="White",activeforeground="Black",activebackground="Pale green")
num2.place(x=80,y=20)

num3 = Button(calc,text="3",command=lambda: click(3),width=10,font="Bold",bg="Black",fg="White",activeforeground="Black",activebackground="Pale green")
num3.place(x=160,y=20)

num4 = Button(calc,text="4",command=lambda: click(4),width=8,font="Bold",bg="Black",fg="White",activeforeground="Black",activebackground="Pale green")
num4.place(x=240,y=20)

num5 = Button(calc,text="5",command=lambda: click(5),width=10,font="Bold",bg="Black",fg="White",activeforeground="Black",activebackground="Pale green")
num5.place(x=0,y=50)

num6 = Button(calc,text="6",command=lambda: click(6),width=10,font="Bold",bg="Black",fg="White",activeforeground="Black",activebackground="Pale green")
num6.place(x=80,y=50)

num7 = Button(calc,text="7",command=lambda: click(7),width=10,font="Bold",bg="Black",fg="White",activeforeground="Black",activebackground="Pale green")
num7.place(x=160,y=50)

num8 = Button(calc,text="8",command=lambda: click(8),width=8,font="Bold",bg="Black",fg="White",activeforeground="Black",activebackground="Pale green")
num8.place(x=240,y=50)

num9 = Button(calc,text="9",command=lambda: click(9),width=10,font="Bold",bg="Black",fg="White",activeforeground="Black",activebackground="Pale green")
num9.place(x=0,y=80)

num0 = Button(calc,text="0",command=lambda: click(0),width=10,font="Bold",bg="Black",fg="White",activeforeground="Black",activebackground="Pale green")
num0.place(x=80,y=80)

def add():
    n1 = entry.get()
    if n1=="":
        n1 = "0"
    global value1
    value1 = int(n1)
    entry.delete(0,END)
    global math
    math = "add"

addition = Button(calc,text="+",command=add,width=10,font="Bold",bg="Black",fg="White")
addition.place(x=160,y=80)

def sub():
    n1 = entry.get()
    if n1=="":
        n1 = "0"
    global value1
    value1 = int(n1)
    entry.delete(0, END)
    global math
    math = "sub"

substract = Button(calc,text="-",command=sub,width=8,font="Bold",bg="Black",fg="White")
substract.place(x=240,y=80)


def mul():
    n1 = entry.get()
    if n1=="":
        n1 = "0"
    global value1
    value1 = int(n1)
    entry.delete(0, END)
    global math
    math = "mul"

multiply = Button(calc,text="*",command=mul,width=10,font="Bold",bg="Black",fg="White")
multiply.place(x=0,y=110)

def devide():
    n1 = entry.get()
    if n1=="":
        n1 = "0"
    global value1
    value1 = int(n1)
    entry.delete(0, END)
    global math
    math = "dev"

divis = Button(calc,text="/",command=devide,width=10,font="Bold",bg="Black",fg="White")
divis.place(x=80,y=110)

def output_val():
   value2 = entry.get()
   if value2 =="":
          value2 = "0"
   entry.delete(0,END)
   global value1
   global math
   result = 0
   if math == "add":
       result = value1+int(value2)
   elif math == "sub":
       result = value1 - int(value2)
   elif math == "mul":
       result = value1 * int(value2)
   elif math == 'dev':
       result = value1// int(value2)
   else:
       result = value2
   entry.insert(0,result)

outputval = Button(calc,text="=",command=output_val,width=10,font="Bold",bg="Green",fg="White")
outputval.place(x=160,y=110)

def clear():
    entry.delete(0,END)

erase = Button(calc,text="clear",command=clear,width=8,bg="red",fg="Black",font="Bold")
erase.place(x=240,y=110)

mainloop()