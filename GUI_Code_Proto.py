import tkinter as tk
from tkinter import Scale, Button
#import serial

# Connect to Arduino
#ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with the appropriate port

def update_positions():
    roll_value = roll_scale.get()
    pitch_value = pitch_scale.get()

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

# Sliders for roll and pitch
roll_scale = Scale(root, from_=-100, to=100, orient="horizontal", label="Roll")
roll_scale.pack(pady=10)

pitch_scale = Scale(root, from_=-100, to=100, orient="horizontal", label="Pitch")
pitch_scale.pack(pady=10)

# Button to update actuator positions
update_button = Button(root, text="Update Positions", command=update_positions)
update_button.pack(pady=20)

# Button to close the serial connection
close_button = Button(root, text="Close Connection", command=ser.close)
close_button.pack(pady=20)

# Run the GUI
root.mainloop()
