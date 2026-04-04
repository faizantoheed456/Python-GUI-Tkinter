from tkinter import *

root = Tk()
root.title("Dropdown menu")
root.iconbitmap("c sharp.ico")
root.geometry("400x400")

def show():
    myLabel = Label(root, text=clicked.get()).pack()

days = [
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday",
    "Saturday"
]

clicked = StringVar()
clicked.set("Monday")

drop = OptionMenu(root, clicked, *days)
drop.pack()

mybtn = Button(root, text="Show me", command=show).pack()
root.mainloop()