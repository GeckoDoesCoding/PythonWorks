#Accept Inputs from user

import tkinter as tk 
from tkinter import ttk
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(2)

window = tk.Tk()

window.title("Label Test Run")

def click_me():
    action.configure(text='Hello ' + name.get())
    action.configure(state='disabled')

# Changing our Label
ttk.Label(window, text="Enter a name:").grid(column=0, row=0)

# Adding a Text box Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(window, width=12, textvariable=name)
name_entered.grid(column=1, row=1)

# Adding a Button
action = ttk.Button(window, text="Click Me!", command=click_me)   
action.grid(column=2, row=1)

							
name_entered.focus()

window.mainloop()