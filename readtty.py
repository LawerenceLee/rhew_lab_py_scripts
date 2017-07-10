#!/usr/bin/python
import subprocess 

# To run me from the command line simply type readtty.
# If permission is denied simply switch to root

usb_port = raw_input("Specify port number: /dev/ttyUSB ")

command = 'python -m serial.tools.miniterm /dev/ttyUSB{}'.format(usb_port)

subprocess.call([command], shell=True)
