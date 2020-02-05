#!/usr/bin/env python3
"""Control an Arduino over the USB port."""

# usb.py
# Created by John Woolsey on 12/17/2019.
# Copyright (c) 2019 Woolsey Workshop.  All rights reserved.


# USB_PORT = "/dev/ttyUSB0"  # Arduino Uno R3 Compatible
USB_PORT = "/dev/ttyACM0"  # Arduino Uno WiFi Rev2


# Imports
import serial


# Functions
def print_commands():
   """Prints available commands."""
   print("Available commands:")
   print("  a - Retrieve Arduino value")
   print("  l - Turn on Arduino LED")
   print("  k - Turn off Arduino LED")
   print("  x - Exit program")


# Main

# Connect to USB serial port at 9600 baud
try:
   usb = serial.Serial(USB_PORT, 9600, timeout=2)
except:
   print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
   print("Exiting program.")
   exit()

# Send commands to Arduino
print("Enter a command from the keyboard to send to the Arduino.")
print_commands()
while True:
   command = input("Enter command: ")
   if command == "a":  # read Arduino A0 pin value
      usb.write(b'read_a0')  # send command to Arduino
      line = usb.readline()  # read input from Arduino
      line = line.decode()  # convert type from bytes to string
      line = line.strip()  # strip extra whitespace characters
      if line.isdigit():  # check if line contains only digits
         value = int(line)  # convert type from string to int
      else:
         print("Unknown value '" + line + "', setting to 0.")
         value = 0
      print("Arduino A0 value:", value)
   elif command == "l":  # turn on Arduino LED
      usb.write(b'led_on')  # send command to Arduino
      print("Arduino LED turned on.")
   elif command == "k":  # turn off Arduino LED
      usb.write(b'led_off')  # send command to Arduino
      print("Arduino LED turned off.")
   elif command == "x":  # exit program
      print("Exiting program.")
      exit()
   else:  # unknown command
      print("Unknown command '" + command + "'.")
      print_commands()
