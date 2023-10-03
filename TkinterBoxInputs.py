#Has Scrolled text, widgets, checkboxes and Drop-down lists
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(2)

win = tk.Tk()   
   
win.title("Python GUI")  
win.configure(background= "Black")

a_label = ttk.Label(win, text="A Label")
a_label.grid(column=0, row=0)

def click_me(): 
    action.configure(text='Hello ' + name.get())

ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1, padx =40, pady =20)                          # column 0

action = ttk.Button(win, text="Click Me!", command=click_me)   
action.grid(column=2, row=1)                                # <= change column to 2

ttk.Label(win, text="Choose a number:").grid(column=1, row=0, padx=20, pady=30)

number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20)
number_chosen.grid(column=1, row=1, padx =50, pady=50)
number_chosen.current(0)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=1, row=4, sticky=tk.W, padx=10, pady =10)                   

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="Unchecked", variable=chVarUn)
check2.deselect()
check2.grid(column=2, row=4, sticky=tk.W, padx=10, pady=10)                   

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=3, row=4, sticky=tk.W, padx=20, pady=20)                     

name_entered.focus()      # Place cursor into name Entry

COLOR1 = "Red"
COLOR2 = "Pink"
COLOR3 = "Teal"
COLOR4 = "Grey"
COLOR5 = "Lime"

def Radios():
    Ops = OPchecks.get()
    if Ops == 1: win.configure(background=COLOR1)
    elif Ops == 2: win.configure(background=COLOR2)
    elif Ops == 3: win.configure(background=COLOR3)
    elif Ops == 4: win.configure(background=COLOR4)
    elif Ops == 5: win.configure(background=COLOR5)
    
OPchecks = tk.IntVar()
rad1 = tk.Radiobutton(win, text=COLOR1, variable=OPchecks, value=1, command=Radios)
rad1.grid(column=1, row=5, sticky=tk.W, columnspan=3, padx=50, pady=50)   

rad2 = tk.Radiobutton(win, text=COLOR2, variable=OPchecks, value=2, command=Radios)
rad2.grid(column=2, row=5, sticky=tk.W, columnspan=3, padx=20, pady=20)  

rad3 = tk.Radiobutton(win, text=COLOR3, variable=OPchecks, value=3, command=Radios)
rad3.grid(column=3, row=5, sticky=tk.W, columnspan=3, padx =20, pady=20)

rad4 = tk.Radiobutton(win, text=COLOR4, variable=OPchecks, value=4, command=Radios)
rad4.grid(column=4, row=5, sticky=tk.W, columnspan=3, padx =20, pady=20)

rad5 = tk.Radiobutton(win, text=COLOR5, variable=OPchecks, value=5, command=Radios)
rad5.grid(column=5, row=5, sticky=tk.W, columnspan=3, padx =20, pady=20)

scrol_w = 30
scrol_h = 3
scr =scrolledtext.ScrolledText(win, width = scrol_w, height = scrol_h, wrap = tk.WORD)
scr.grid(column= 0, row= 2, rowspan=4, columnspan= 1, padx =100, pady=100)

win.mainloop()

