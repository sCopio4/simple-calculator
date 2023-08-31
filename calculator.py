from tkinter import *
from functools import partial

tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('KC Mathematical Operation')

def add():
    num1 = Label1Entry.get()
    num2 = Label2Entry.get()
    resultShow.configure(text = int(num1) + int(num2))
    print(int(num1) + int(num2))
    
def sub():
    num1 = Label1Entry.get()
    num2 = Label2Entry.get()
    resultShow.configure(text = int(num1) - int(num2))
    print(int(num1) - int(num2))  

def mul():
    num1 = Label1Entry.get()
    num2 = Label2Entry.get()
    resultShow.configure(text = int(num1) * int(num2))
    print(int(num1) * int(num2))  

def div():
    num1 = Label1Entry.get()
    num2 = Label2Entry.get()
    resultShow.configure(text = int(num1) / int(num2))
    print(int(num1) / int(num2))  
    

showTxt = Label(tkWindow, text= "Mathematical Operation", fg="Steel Blue", bd = 2, font=("Arial Black", 30))
showTxt.grid(row=0, column= 0, columnspan=4)

Label1 = Label(tkWindow, text= "Enter the First Number: ", font=("Arial Balck", 10))
Label1.grid(row=1, column= 0, sticky= E)

Label1Entry = Entry(tkWindow, width=60)
Label1Entry.grid(row=1,column = 1, columnspan=3, sticky = N)


Label2 = Label(tkWindow, text= "Enter the Second Number: ", font=("Arial Balck", 10))
Label2.grid(row=2, column= 0, sticky= E)

Label2Entry = Entry(tkWindow, width=60)
Label2Entry.grid(row=2,column = 1, columnspan=3, sticky = N)

#buttons
addButton = Button(tkWindow, text= "Add", command= add, padx = 30)
addButton.grid(row=3, column=0)

subButton = Button(tkWindow, text= "Sub", command= sub, padx = 30)
subButton.grid(row=3, column=1)

mulButton = Button(tkWindow, text= "Mul", command= mul, padx = 30)
mulButton.grid(row=3, column=2)

divButton = Button(tkWindow, text= "Div", command= div, padx = 30)
divButton.grid(row=3, column=3)


result = Label(tkWindow, text = "Result:")
result.grid(row=4, column=0)

resultShow = Label(tkWindow)
resultShow.grid(row=4, column=1)

tkWindow.mainloop()

