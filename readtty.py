#!/usr/bin/python
import subprocess 

# To run me from the command line simply type readtty.
# If permission is denied simply switch to root

usb_type = '' 

type_selection = raw_input("Select [A] ttyUSB, [B] ttyS ").upper() 
if type_selection == 'A':
	usb_type = 'ttyUSB'
elif type_selection == 'B':
	usb_type = 'ttyS'

usb_port = raw_input("Specify port number: ")

command = 'python -m serial.tools.miniterm /dev/tty{}{}'.format(usb_type, usb_port)

subprocess.call([command], shell=True)
