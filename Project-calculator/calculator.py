from tkinter import *
# creating windows to work on
root = Tk()
# title of the application
root.title("Nashari Simple Calculater")
#root.iconbitmap("C:\Users\Dell\Google Drive\Python\Python\tkinder\Project-calculator")


global f_num

# creating text field to show the results of calculation

e = Entry(root, width=70, borderwidth=1)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# defining the function of buttons


def button_click(number):
    # e.delete(0, END)  # its delete the text in widget textbox from 0 to END

    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


# for clearing the textbox widget


def clear_button():
    e.delete(0, END)


def add_button():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def minus_button():
    first_number = e.get()
    global f_num
    global math
    math = "substruction"
    f_num = int(first_number)
    e.delete(0, END)


def multiply_button():
    first_number = e.get()
    global f_num
    global math
    math = "mutiplication"
    f_num = int(first_number)
    e.delete(0, END)


def divide_button():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


def percentage_button():
    first_number = e.get()
    global f_num
    global math
    math = "percentage"
    f_num = int(first_number)
    e.delete(0, END)


def power_button():
    first_number = e.get()
    global f_num
    global math
    math = "power"
    f_num = int(first_number)
    e.delete(0, END)

# addition of two no numbers


def equal_button():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "substruction":
        e.insert(0, f_num - int(second_number))
    if math == "mutiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))
    if math == "percentage":
        e.insert(0, (f_num / 100)*int(second_number))
    if math == "power":
        e.insert(0, f_num * f_num)


# creating buttons

button1 = Button(root, text="1", padx=45, pady=20,
                 command=lambda: button_click(1))
button2 = Button(root, text="2", padx=45, pady=20,
                 command=lambda: button_click(2))
button3 = Button(root, text="3", padx=45, pady=20,
                 command=lambda: button_click(3))
button4 = Button(root, text="4", padx=45, pady=20,
                 command=lambda: button_click(4))
button5 = Button(root, text="5", padx=45, pady=20,
                 command=lambda: button_click(5))
button6 = Button(root, text="6", padx=45, pady=20,
                 command=lambda: button_click(6))
button7 = Button(root, text="7", padx=45, pady=20,
                 command=lambda: button_click(7))
button8 = Button(root, text="8", padx=45, pady=20,
                 command=lambda: button_click(8))
button9 = Button(root, text="9", padx=45, pady=20,
                 command=lambda: button_click(9))
button0 = Button(root, text="0", padx=45, pady=20,
                 command=lambda: button_click(0))
buttondot = Button(root, text=".", padx=45, pady=20,
                   command=lambda: button_click("."))
button_plusmin = Button(root, text="+/-", padx=40,
                        pady=20, command=button_click)
button_plus = Button(root, text="+", padx=45, pady=20,
                     command=add_button)
button_minus = Button(root, text="-", padx=45, pady=20,
                      command=minus_button)
button_multiply = Button(root, text="*", padx=45, pady=20,
                         command=multiply_button)
button_divide = Button(root, text="/", padx=45, pady=20,
                       command=divide_button)
button_equals = Button(root, text="=", padx=45, pady=20,
                       command=equal_button)
button_clear = Button(root, text="clear", padx=35,
                      pady=20, command=clear_button)
button_percentage = Button(root, text="%", padx=35,
                           pady=20, command=percentage_button)
button_power = Button(root, text="x^", padx=35,
                      pady=20, command=power_button)

# pasting the above buttons on work field

button1.grid(row=5, column=0)
button2.grid(row=5, column=1)
button3.grid(row=5, column=2)

button4.grid(row=4, column=0)
button5.grid(row=4, column=1)
button6.grid(row=4, column=2)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)

button0.grid(row=6, column=1)
buttondot.grid(row=6, column=2)
button_plusmin.grid(row=6, column=0)
button_plus.grid(row=5, column=4)
button_minus.grid(row=4, column=4)
button_multiply.grid(row=3, column=4)
button_divide.grid(row=2, column=4)
button_equals.grid(row=6, column=4)
button_clear.grid(row=2, column=0)
button_percentage.grid(row=2, column=1)
button_power.grid(row=2, column=2)

root.mainloop()
