from tkinter import *

# Create the main window
root = Tk()
root.title("Entry widget Demo")
root.geometry("400x200")

#1. Create a stringVar to hold the input
user_input = StringVar()

#2. Create an entry widget
entry_box = Entry(
    root,
    textvariable=user_input,
    width=30,
    borderwidth=3,
    bg='lightyellow',
    fg='darkblue'
)

#Place the entry using grid
entry_box.grid(row=0, column=0, padx=10, pady=10, sticky='w')

#3. A function that takes input and displays a greeting
def displayGreet():

    name = user_input.get()
    if name.strip():
        greeting = f"Hello, {name}!"
    else:
        greeting = "Please enter a name"

    output_label.config(text=greeting)

#4: A button to trigger a greeting
greet_button = Button(
    root,
    text="Say Hello", 
    command=displayGreet,
    padx=10,
    pady=5,
    bg='lightblue'
)

greet_button.grid(row=1, column=0, pady=5)

#5: A label to display the text
output_label = Label(root, text="", font=("Arial", 12))
output_label.grid(row=2, column=0, pady=10)

root.mainloop()