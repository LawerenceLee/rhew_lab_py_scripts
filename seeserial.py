#!/usr/bin/python
import subprocess 

# To run me from the command line simply type seeserial.
# If permission is denied simply switch to root

command = 'python -m serial.tools.list_ports'

subprocess.call([command], shell=True)


