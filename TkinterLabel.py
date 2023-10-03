#label, button, click and watch the colour change

import tkinter as tk 
from tkinter import ttk

window = tk.Tk()

window.title("Label Test Run")

L1 = ttk.Label(text=" Guten Morgen")
L1.grid(column=0, row=0)

def Clicked():
    clicker.configure(text="Clicked")
    L1.configure(foreground='red')
    L1.configure(text = 'Colour Changed')

clicker =  ttk.Button( window, text="It's the Clicker", command= Clicked)
clicker.grid(column=1, row=0)   

window.mainloop()