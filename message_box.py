from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message box")

#showinfo, showerror, showwarning. askquestion, askokcancel, askyesno
def popup():
    response = messagebox.askyesno("This is my popup", "Hello, World")

    if response == 1:
        Label(root, text="You clicked Yes!").pack()
    else:
        Label(root, text="You clicked No!").pack()


Button(root, text="Popup", command= popup).pack()

root.mainloop()