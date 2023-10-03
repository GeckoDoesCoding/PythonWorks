import tkinter as tk
from tkinter import ttk
window = tk.Tk()
#window.resizable(0,0)
window.title('Hello')

#ttk.Label(window, text="Testing") .grid(column = 0, row = 0)
Label1 = ttk.Label(window, text="Testing").grid(column =0, row = 0)

def ClickMe():
    action.configure(text = "Tested")
    #Label1.configure(foreground = 'red')

action = ttk.Button(window, text = 'Test This', command =ClickMe)
action.grid(column =1, row =0)


window.mainloop()


#greeting = tk.Label(text = "Hello Tkinter")
#greeting.pack()
