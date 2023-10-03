import PySimpleGUI as sg

layout = [[sg.Text('Persistent window')],      
          [sg.Input(key='-IN-')],      
          [sg.Submit(), sg.Exit()]]      

window = sg.Window('Window that stays open', layout)      

while True:                             
    event, values = window.read() 
    print(event, values)       
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
        break

