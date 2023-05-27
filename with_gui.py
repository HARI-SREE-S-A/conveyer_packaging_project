import serial
import time
from tkinter import Tk, Button, Label, OptionMenu, StringVar

# Serial communication settings
SERIAL_PORT = '/dev/ttyACM0'  # Change this to your Arduino serial port
BAUD_RATE = 9600

# GUI settings
WINDOW_TITLE = "Weighing and Filling Automation"
FONT = ('Arial', 14)
WEIGHT_LABEL_TEXT = "Weight (g):"
THING_LABEL_TEXT = "Thing:"

# Arduino commands
START_COMMAND = '1'
STOP_COMMAND = '0'

# Initialize the serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # Wait for the Arduino to initialize

# Create the GUI window
window = Tk()
window.title(WINDOW_TITLE)

# Variables
weight = 0
selected_thing = StringVar()
selected_thing.set("Type 1")  # Default selection

# GUI elements
weight_label = Label(window, text=WEIGHT_LABEL_TEXT, font=FONT)
weight_label.pack()

weight_value_label = Label(window, text=str(weight), font=FONT)
weight_value_label.pack()

thing_label = Label(window, text=THING_LABEL_TEXT, font=FONT)
thing_label.pack()

thing_option_menu = OptionMenu(window, selected_thing, "Type 1", "Type 2", "Type 3")
thing_option_menu.pack()


start_button = Button(window, text="Start", font=FONT)
start_button.pack()

stop_button = Button(window, text="Stop", font=FONT)
stop_button.pack()


# Event handler for the start button
def start_button_clicked():
    selected_thing_value = selected_thing.get()
    command = START_COMMAND + selected_thing_value[5:]  # Extract type number from the selected thing
    ser.write(command.encode())


# Event handler for the stop button
def stop_button_clicked():
    ser.write(STOP_COMMAND.encode())


# Update the weight value label
def update_weight_label():
    global weight
    ser.write(b'w')  # Request the current weight from Arduino
    response = ser.readline().strip().decode()
    if response.isdigit():
        weight = int(response)
        weight_value_label.config(text=str(weight))
    window.after(100, update_weight_label)


# Bind event handlers to buttons
start_button.config(command=start_button_clicked)
stop_button.config(command=stop_button_clicked)

# Start updating the weight value label
update_weight_label()

# Start the GUI event loop
window.mainloop()

# Clean up
ser.close()

