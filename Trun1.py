import PySimpleGUI as sg      

sg.theme('BlueMono')
layout = [
    [sg.Text('Enter Roll & Pitch Values')],
    [sg.Text('Roll', size =(10, 1)), sg.InputText()],
    [sg.Text('Pitch', size =(10, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]   
window = sg.Window('TestRun1', layout)    
while True:
    event, values = window.read()    
    if event == 'Cancel':
        window.close()
    else:
        if(values[0].isnumeric() & values[1].isnumeric()):
            sg.popup('Values noted successfully')      
        else:
            sg.popup('Invalid Values')
            


