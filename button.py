import PySimpleGUI as sg

layout = [[sg.Text("Test Run 1")], [sg.Button("Ack")]]
window = sg.Window("Demo", layout)

while True:
    event, values = window.read()
    if event == "Ack" or event == sg.WIN_CLOSED:
        break
    
window.close()
