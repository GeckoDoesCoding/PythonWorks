import tkinter as tk
from ctypes import windll
root = tk.Tk()

label = tk.Label(text="Hello, Tkinter", fg="blue", bg="yellow", height=40, width=80)
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="white",
    fg="black",
)

label2 = tk.Label(text="Name")
entry = tk.Entry(fg="black", bg="white", width=50)

label.pack()
button.pack()
label2.pack()
entry.pack()


try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()










