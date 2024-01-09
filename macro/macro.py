import time
import os
import board
from digitalio import DigitalInOut, Pull
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import gui

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# Defining the keywords for the macro scripts
class keywords:
    def SLEEP(sleep_time):
        time.sleep(float(sleep_time))
    
    def WRITE(text):
        layout.write(text, 0.065)
    
    def SEND(keys):
        keys = keys.split("+")
        # Loop through all the keys and turn them into a list of keycodes
        keycodes = []
        for key in keys:
            keycodes.append(getattr(Keycode, key.strip()))

        # Send the keycodes
        keyboard.send(*keycodes)
    
    def DEBUG(text):
        print(text)

def open_macro_file(macro_file):
    # Open the file
    with open(macro_file) as file:
        # Go through each of the lines
        for command in file.readlines():
            # Remove commments
            command = command.split("#")[0]

            # Split the commmand and the argument into different variables
            split = command.replace('\n', '').split(":")
            command = split[0].strip()
            argument = split[1].strip()
            
            # Get the function from the keywords class
            command_function = getattr(keywords, command)
            
            # Run the function
            command_function(argument)

def create_menu():
    macros = {}
    for macro in os.listdir("/macro/macros"):
        macros[macro] = [open_macro_file, "/macro/macros/" + macro]
    
    return(macros)