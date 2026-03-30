from tkinter import *

#Create the main window
root = Tk()

#Create a widget label with text
mylabel = Label(root, text='Hello, World!')

#Shoving it onto the screen
mylabel.pack()

#Start the event loop
root.mainloop()