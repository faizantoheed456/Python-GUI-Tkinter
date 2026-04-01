from tkinter import *

root = Tk()
root.title("Learn Tkinter")
root.iconbitmap("c sharp.ico")

TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
    ("Cheese", "Cheese")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()
    


my_button = Button(root, text="Click me!", command=lambda: clicked(pizza.get()))
my_button.pack()

root.mainloop()