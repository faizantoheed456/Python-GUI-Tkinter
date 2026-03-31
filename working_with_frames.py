from tkinter import *


root = Tk()
root.title('Learn C#')
root.iconbitmap('c sharp.ico') #Displaying icon

my_frame = LabelFrame(root, text="Learn C#", padx=10, pady=10)
my_frame.pack(padx=10, pady=10)


b = Button(my_frame, text="Don't click here", padx=10, pady=10)
c = Button(my_frame, text="Or here", padx=10, pady=10)
b.grid(row=0, column=0)
c.grid(row=1, column=1)
#b.pack()

root.mainloop()