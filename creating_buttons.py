from tkinter import *

# Create the main window
root = Tk()
root.title("Button Demo")
root.geometry("300x200")

# Function to be called when the button is clicked
def show_message():
    
    message_label = Label(root, text="Button was clicked!", fg="white", bg="green")
    message_label.grid(row=1, column=0, pady=10)

# Create a button widget
my_button = Button(
    root,
    text="Click Me",
    state=NORMAL,          
    padx=20,               
    pady=10,               
    fg="white",            
    bg="blue",             
    command=show_message   
)

# Place the button in the window using grid
my_button.grid(row=0, column=0, padx=20, pady=20)

# Start the main event loop
root.mainloop()