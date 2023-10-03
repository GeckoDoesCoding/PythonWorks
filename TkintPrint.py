
import tkinter as tk
from tkinter import *
root = tk.Tk()
label = tk.Label(text="Value")
entry=tk.Entry()

label.pack()
entry.pack()

val = entry.get()
print(val)
