from tkinter import *

root = Tk()
root.title("Learn Tkinter")
root.iconbitmap("c sharp.ico")

r = IntVar()
r.set("2")

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()
    

Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

myLabel = Label(root, text=r.get())
my_button = Button(root, text="Click me!", command=lambda: clicked(r.get()))
myLabel.pack()
my_button.pack()

root.mainloop()