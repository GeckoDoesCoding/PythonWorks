import tkinter as tk
from tkinter import Canvas, Button
#import serial

# Connect to Arduino
#ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with the appropriate port

def update_positions():
    roll_value = roll_knob.get()
    pitch_value = pitch_knob.get()

    # Perform calculations or mapping based on roll and pitch values
    # Adjust the following lines based on your specific requirements
    actuator1_pos = roll_value + pitch_value
    actuator2_pos = roll_value - pitch_value
    actuator3_pos = -roll_value + pitch_value
    actuator4_pos = -roll_value - pitch_value

    # Send positions to Arduino
    #ser.write(f"{actuator1_pos},{actuator2_pos},{actuator3_pos},{actuator4_pos}\n".encode())

# Create GUI
root = tk.Tk()
root.title("Actuator Control")

# Function to create circular knob
def create_knob(canvas, value_var):
    knob = Canvas(canvas, width=100, height=100, bg='white')
    knob.create_oval(10, 10, 90, 90, outline='black', width=2)
    knob.create_text(50, 50, text=value_var.get())
    return knob

# Knobs for roll and pitch
roll_var = tk.IntVar()
pitch_var = tk.IntVar()

roll_knob = create_knob(root, roll_var)
roll_knob.pack(pady=10)
roll_var.set(0)

pitch_knob = create_knob(root, pitch_var)
pitch_knob.pack(pady=10)
pitch_var.set(0)

# Button to update actuator positions
update_button = Button(root, text="Update Positions", command=update_positions)
update_button.pack(pady=20)

# Button to close the serial connection
close_button = Button(root, text="Close Connection")#, command=ser.close)
close_button.pack(pady=20)

# Run the GUI
root.mainloop()
