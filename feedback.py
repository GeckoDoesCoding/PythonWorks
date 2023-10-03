import PySimpleGUI as sg      

layout = [[sg.Text('Enter Input')],      
                 [sg.InputText()],      
                 [sg.Submit(), sg.Cancel()]]      

window = sg.Window('Title', layout)    

event, values = window.read()    
window.close()

text_input = values[0]    
sg.popup('You Have Entered: ', text_input)
