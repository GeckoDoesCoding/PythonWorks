import PySimpleGUI as sg      
import socket
from time import ctime
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(2)

# PySimpleGUI
#has Magna Logo
#Uses Sockets for communication
#works

sg.theme("black")
layout = [
    [sg.Text('Enter Roll & Pitch Values', size=(25,1), font=("72", 15))],
    [sg.Text('Roll: ', size =(15, 1), font=("72", 12)), sg.InputText(size=(25,1), focus= True)],
    [sg.Text('Pitch: ', size =(15, 1), font=("72", 12)), sg.InputText(size=(25,1), focus= True)],
    [sg.Submit(), sg.Cancel()],
    [sg.Text(ctime())]
]  
window = sg.Window('TestRun1', layout, icon='c:/Users/shoukulk/Desktop/work/Logos/MagnaLogo.ico')   
  
while True:
    event, values = window.read()#type:ignore
    if event == 'Cancel':
        window.close()
    else:
      
       
      if(values[0].isnumeric() and values[1].isnumeric()): # type : ignore
            a = int(float(values[0]))
            b = int(float(values[1]))  
           
            if(a > 20 or b > 20):
                sg.popup('Enter Values Below 20', icon='c:/Users/shoukulk/Desktop/work/Logos/MagnaLogo.ico')
            
            else:
                s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.bind((socket.gethostname(), 1221) )
                s.listen(5)
                clientsocket, address = s.accept() 
                sg.popup('Values Noted Successfully', icon='c:/Users/shoukulk/Desktop/work/Logos/MagnaLogo.ico')
                print(f"Connection from {address} has been established")
                clientsocket.send(bytes(str(a), "utf-8"))
                clientsocket.send(bytes(str(b), "utf-8"))                              
      else:
            sg.popup('Only Integer Inputs are Accepted', icon='c:/Users/shoukulk/Desktop/work/Logos/MagnaLogo.ico')