from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn C#')
root.iconbitmap('c sharp.ico') #Displaying icon

my_image = ImageTk.PhotoImage(Image.open('discord.png')) #Displaying image
my_label = Label(image=my_image)
my_label.pack()

exit_button = Button(root, text='Exit button', command=root.quit) #Exit button
exit_button.pack()
root.mainloop()