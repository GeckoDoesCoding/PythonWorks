import PySimpleGUI as sg

def rotate_servo(angle, speed):
    # Implement your servo rotation logic here
    pass

# GUI layout
layout = [
    [sg.Text('Enter Angle (0 to 180):'), sg.InputText(key='-ANGLE-', size=(10, 1))],
    [sg.Text('Enter Speed (1 to 5):'), sg.InputText(key='-SPEED-', size=(10, 1))],
    [sg.Button('Rotate Counterclockwise', key='-CCW-'), sg.Button('Rotate Clockwise', key='-CW-')],
    [sg.Button('About'), sg.Button('QUIT')],
]

# Create the window
window = sg.Window('Servo Motor Control', layout)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'QUIT':
        break

    elif event == 'About':
        sg.popup('Logic Don\'t Care Software\nServo Motor Ver 1.0\nAugust 2022', title='About')

    elif event in ('-CCW-', '-CW-'):
        try:
            angle = int(values['-ANGLE-'])
            speed = int(values['-SPEED-'])
            if 0 <= angle <= 180 and 1 <= speed <= 5:
                if event == '-CCW-':
                    rotate_servo(angle, speed)
                elif event == '-CW-':
                    rotate_servo(angle, speed)
            else:
                sg.popup_error('Invalid angle or speed values. Please enter valid numeric values.')
        except ValueError:
            sg.popup_error('Invalid input. Please enter valid numeric values.')

# Close the window
window.close()
