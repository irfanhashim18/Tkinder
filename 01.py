from tkinter import *
import datetime

root = Tk()
text_field = Entry(root)
text_field.grid(row=8, column=0)

mylabel = Label(root, text="Golden ARS Catering")
mylabel1 = Label(root, text="how are you").grid(row=1, column=1)
mylabel2 = Label(root, text=" i am good")
mylabel3 = Label(root, text="how are you today")
mylabel4 = Label(root, text="today is raining")


mylabel.grid(row=0, column=0)
#mylabel1.grid(row=1, column=1)
mylabel2.grid(row=2, column=2)
mylabel3.grid(row=3, column=3)
mylabel4.grid(row=4, column=0)

# creating buttons


def tables(x):
    a = [x * i for i in range(1, 11)]
    print(a)


def button2():
    mybutton2 = Button(root, text=tables(10))
    mybutton2.grid(row=6, column=0)


def lebalbybutton():
    mylebal5 = Label(root, text=tables(10))
    mylebal5.grid(row=7, column=0)


mybutton = Button(root, text="button", padx=50,
                  command=lebalbybutton, fg="red", bg="yellow")
# change the size of button with padx and pady

mybutton.grid(row=5, column=0)

root.mainloop()
