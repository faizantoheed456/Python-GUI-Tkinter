from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.geometry("500x500")

my_image_1 = ImageTk.PhotoImage(Image.open("my_img1.png").resize((500,300)))
my_image_2 = ImageTk.PhotoImage(Image.open("my_img2.png").resize((500,300)))
my_image_3 = ImageTk.PhotoImage(Image.open("my_img3.png").resize((500,300)))
my_image_4 = ImageTk.PhotoImage(Image.open("my_img4.png").resize((500,300)))
my_image_5 = ImageTk.PhotoImage(Image.open("my_img5.png").resize((500,300)))

my_images = [my_image_1, my_image_2, my_image_3, my_image_4, my_image_5]

my_label = Label(image=my_image_1)
my_label.grid(row=0, column=0, columnspan=3)

def foward_click(image_number):
    global my_label
    global forward_button
    global backward_button

    my_label.grid_forget()
    my_label = Label(image=my_images[image_number-1])
    forward_button = Button(root, text=">>", command=lambda: foward_click(image_number+1))
    backward_button = Button(root, text="<<", command=lambda: back_click(image_number-1))

    if image_number == 5:
        forward_button = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    forward_button.grid(row=1, column=2)
    backward_button.grid(row=1, column=0)


def back_click(image_number):
    global my_label
    global forward_button
    global backward_button

    my_label.grid_forget()
    my_label = Label(image=my_images[image_number-1])
    forward_button = Button(root, text=">>", command=lambda: foward_click(image_number+1))
    backward_button = Button(root, text="<<", command=lambda: back_click(image_number-1))

    if image_number == 1:
        backward_button = Button(root, text="<<", state=DISABLED)
        
    my_label.grid(row=0, column=0, columnspan=3)
    forward_button.grid(row=1, column=2)
    backward_button.grid(row=1, column=0)


forward_button = Button(root, text=">>", command=lambda: foward_click(2))
backward_button = Button(root, text="<<", command=back_click, state=DISABLED)
exit_button = Button(root, text='Exit button', command=root.quit)

forward_button.grid(row=1, column=2)
backward_button.grid(row=1, column=0)
exit_button.grid(row=1, column=1)

root.mainloop()