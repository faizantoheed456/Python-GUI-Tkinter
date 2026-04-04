from tkinter import *

root = Tk()
root.title("Sliders")
root.iconbitmap("c sharp.ico")
root.geometry("400x400")

def check():
    my_label = Label(root, text=var.get()).pack()
var = StringVar()

v = Checkbutton(root, text="Would you like to supersize your order? Check here!", variable=var, onvalue="Super size", offvalue="Regular")
v.deselect()
v.pack()

my_btn = Button(root, text="Click me!", command=check).pack()

root.mainloop()