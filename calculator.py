from tkinter import *

#Creating a window, giving title and set its dimension
root = Tk()
root.title('Calculator')
root.geometry("300x500")
root.configure(bg='#202020') 

e = Entry(root, width=45, borderwidth=10)
e.grid(row=0, column=0, columnspan=3, pady=10)

def button_click(number):
    
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():

    e.delete(0, END)

def button_add():

    first_number = e.get()
    global f_num 
    f_num = int(first_number)
    global math
    math = "addition"
    e.delete(0, END)

def button_equal():

    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
        
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    
    if math == "division":
        e.insert(0, f_num / int(second_number))


def button_subtract():
    
    first_number = e.get()
    global f_num 
    f_num = int(first_number)
    global math
    math = "subtraction"
    e.delete(0, END)

def button_multiply():
    
    first_number = e.get()
    global f_num 
    f_num = int(first_number)
    global math
    math = "multiplication"
    e.delete(0, END)

def button_divide():
    
    first_number = e.get()
    global f_num 
    f_num = int(first_number)
    global math
    math = "division"
    e.delete(0, END)


#Creating buttons
button1 = Button(root, text="7", bg='#2D2D2D', fg='#FFFFFF', padx=40, pady=20, command=lambda: button_click(7))
button2 = Button(root, text="8", bg='#2D2D2D', fg='#FFFFFF', padx=40, pady=20, command=lambda: button_click(8))
button3 = Button(root, text="9", bg='#2D2D2D', fg='#FFFFFF', padx=40, pady=20, command=lambda: button_click(9))

button4 = Button(root, text="4", bg='#2D2D2D', fg='#FFFFFF', padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", bg='#2D2D2D', fg='#FFFFFF', padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", bg='#2D2D2D', fg='#FFFFFF', padx=40, pady=20, command=lambda: button_click(6))

button7 = Button(root, text="1", bg='#2D2D2D', fg='#FFFFFF', padx=40, pady=20, command=lambda: button_click(1))
button8 = Button(root, text="2", bg='#2D2D2D', fg='#FFFFFF', padx=40, pady=20, command=lambda: button_click(2))
button9 = Button(root, text="3", bg='#2D2D2D', fg='#FFFFFF', padx=40, pady=20, command=lambda: button_click(3))

button0 = Button(root, text="0", bg='#2D2D2D', fg='#FFFFFF', padx=40, pady=20, command=lambda: button_click(0))
buttonAdd = Button(root, text="+", bg='#252525', fg='#FF9500', padx=40, pady=20, command=button_add)
buttonSubtract = Button(root, text="-", bg='#252525', fg='#FF9500', padx=40, pady=20, command=button_subtract)
buttonMultiply = Button(root, text="*", bg='#252525', fg='#FF9500', padx=40, pady=20, command=button_multiply)
buttonDivide = Button(root, text="/", bg='#252525', fg='#FF9500', padx=39, pady=20, command=button_divide)
buttonEqual = Button(root, text="=", bg='#252525', fg='#FF9500', padx=90, pady=20, command=button_equal)
buttonClear = Button(root, text="clear", bg='#252525', fg='#FF9500', padx=79, pady=20, command=button_clear)

#Setting buttons on screen
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)

button0.grid(row=4, column=0)
buttonAdd.grid(row=5, column=0)
buttonEqual.grid(row=4, column=1, columnspan=2)
buttonClear.grid(row=6, column=1, columnspan=2)
buttonSubtract.grid(row=5, column=1)
buttonMultiply.grid(row=5, column=2)
buttonDivide.grid(row=6, column=0)


root.mainloop()