#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess 

# To run me from the command line simply type seeserial.
# If permission is denied simply switch to root

def main():
	command = 'python -m serial.tools.list_ports -v'
	subprocess.call([command], shell=True)

	symlink_list = ['omegaSampleTrap', 'omegaWaterTrap', 'valcoVici6Port']

	for link in symlink_list:
		symlink_command = 'ls -al /dev/{}'.format(link)
		subprocess.call([symlink_command], shell=True)
	print('\n')


if __name__ == "__main__":
	main()


