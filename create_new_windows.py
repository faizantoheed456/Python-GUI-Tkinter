from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Creating new windows")
root.iconbitmap("c sharp.ico")

def clicked():
    global my_image
    my_win = Toplevel()
    my_win.title("Creating new windows")
    my_image = ImageTk.PhotoImage(Image.open("my_img4.png").resize((500,300)))
    lbl = Label(my_win, image=my_image).pack()
    btn = Button(my_win, text="Exit", command= my_win.destroy).pack()

button = Button(root, text="Click me", command= clicked).pack()
root.mainloop()