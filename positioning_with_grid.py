from tkinter import *

#Create the main window
root = Tk()

#Create a widget label with text
mylabel1 = Label(root, text='Hello, World!')
mylabel2 = Label(root, text='My name is Faizan Toheed')

#Shoving it onto the screen
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=5)

#Start the event loop
root.mainloop()