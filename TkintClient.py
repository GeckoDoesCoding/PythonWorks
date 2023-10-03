import socket
import tkinter as tk 
from tkinter import ttk
from tkinter import *

window = tk.Tk()
logo = PhotoImage(file= 'C:/Users/shoukulk/Desktop/work/Logos/MagnaLogo.png')
window.iconphoto(False, logo)
#window.resizable(0,0)
window.title('Hello')

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
#ttk.Label(window, text="Testing") .grid(column = 0, row = 0)
Label1 = ttk.Label(window, text="Testing").grid(column =0, row = 0)

def ClickMe():
    action.configure(text = "Tested")   
    s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1221))
    msg =s.recv(1024)
    print(msg.decode("utf-8"))
    #Label1.configure(foreground = 'red')

action = ttk.Button(window, text = 'Test This', command =ClickMe)
action.grid(column =1, row =0)
window.mainloop()

