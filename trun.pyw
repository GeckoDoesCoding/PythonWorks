import PySimpleGUI as sg      

sg.theme('Topanga')
layout = [
    [sg.Text('Enter Roll & Pitch Values')],
    [sg.Text('Roll', size =(15, 1)), sg.InputText()],
    [sg.Text('Pitch', size =(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]   
window = sg.Window('TestRun1', layout)    
while True:
    event, values = window.read()    
    if event == 'Cancel':
        window.close()
    else:
        sg.popup('Roll&Pitch Entered:', values[0], values[1]) 




