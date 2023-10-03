import PySimpleGUI as sg

sg.theme('Systemd')

layout = [
    [sg.Text('Please enter your Phone')],
    [sg.Text('Phone', size=(15, 1)), sg.InputText(key="lp1")],
    [sg.Button("Input"), sg.Quit()]
]
window = sg.Window('Simple data entry window', layout)
while True:

    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, "Quit"):
        window.close()
        break
    elif event == "Input":
        text = values['lp1']
        if text == '':
            print('Null string')
        else:
            try:
                value = int(text)
                print(f'Integer: {value}')
            except:
                sg.popup("Invalid")
                

window.close()