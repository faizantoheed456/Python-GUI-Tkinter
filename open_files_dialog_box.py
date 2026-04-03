from tkinter import *
#For images
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Opening files")
root.iconbitmap("c sharp.ico")

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="E:\tkinter", title="Open files", filetypes=(("PNG files", "*.png"), ("All files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename).resize((300, 300)))
    my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text='Open file', command= open).pack()
root.mainloop()