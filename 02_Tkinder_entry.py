from tkinter import *

# input fields
root = Tk()
e1 = Entry(root, width=50, fg="blue", bg="yellow", borderwidth=2)
e1.pack()
e1.get()
e1.insert(0, "Please enter your name:")


def lebaltext():
    lebaltext1 = Label(root, text=f' hellow {e1.get()} , how are you today')
    lebaltext1.pack()


button1 = Button(root, text="Submit your name", padx=50, command=lebaltext)
button1.pack()


root.mainloop()
