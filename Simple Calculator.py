from tkinter import *

global f_num
global math

calculate = Tk()

calculate.title("Simple Calculator")

e = Entry(calculate, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=15, pady=15)


def button_work(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


def button_equals():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    elif math == "subtraction":
        e.insert(0, f_num - int(second_number))

    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))

    elif math == "division":
        e.insert(0, f_num / int(second_number))


# defining buttons


button_1 = Button(calculate, text="1", padx="50", pady="30", command=lambda: button_work(1))
button_2 = Button(calculate, text="2", padx="50", pady="30", command=lambda: button_work(2))
button_3 = Button(calculate, text="3", padx="50", pady="30", command=lambda: button_work(3))
button_4 = Button(calculate, text="4", padx="50", pady="30", command=lambda: button_work(4))
button_5 = Button(calculate, text="5", padx="50", pady="30", command=lambda: button_work(5))
button_6 = Button(calculate, text="6", padx="50", pady="30", command=lambda: button_work(6))
button_7 = Button(calculate, text="7", padx="50", pady="30", command=lambda: button_work(7))
button_8 = Button(calculate, text="8", padx="50", pady="30", command=lambda: button_work(8))
button_9 = Button(calculate, text="9", padx="50", pady="30", command=lambda: button_work(9))
button_0 = Button(calculate, text="0", padx="50", pady="30", command=lambda: button_work(0))

button_add = Button(calculate, text="+", padx="50", pady="30", command=button_add)
button_subtract = Button(calculate, text="-", padx="50", pady="30", command=button_subtract)
button_multiply = Button(calculate, text="*", padx="50", pady="30", command=button_multiply)
button_divide = Button(calculate, text="/", padx="50", pady="30", command=button_divide)
button_clear = Button(calculate, text="clear", padx="40", pady="30", command=button_clear)
button_equals = Button(calculate, text="equal", padx="150", pady="30", command=button_equals)

# displaying buttons


button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)

button_multiply.grid(row=5, column=0)
button_divide.grid(row=5, column=1)
button_clear.grid(row=5, column=2)

button_equals.grid(row=6, column=0, columnspan=3)

calculate.mainloop()
