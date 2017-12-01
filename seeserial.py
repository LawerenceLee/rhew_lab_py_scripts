#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess 


def list_ports():
    """Uses a python built-in to search for connected USB devices"""
    command = 'python -m serial.tools.list_ports -v'
    subprocess.call([command], shell=True)


def check_FID_devices():
    
    print('\nSYMLINKs Connected:')
    symlink_list = ['omegaSampleTrap', 'omegaWaterTrap', 'valcoVici6Port', 'redyFlowMeter']

    for link in symlink_list:
	try:
	    symlink_command = 'ls -al /dev/{}'.format(link)
	    subprocess.call([symlink_command], shell=True)
	except Exception as e:
	    print(e, '\n')
    print('\n')
	

def main():
    list_ports()
    check_FID_devices()


if __name__ == "__main__":
    main()
