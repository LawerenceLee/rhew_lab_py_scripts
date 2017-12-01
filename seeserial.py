#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess 


def list_ports():
    """Uses a python built-in to search for connected USB devices."""
    command = 'python -m serial.tools.list_ports -v'
    subprocess.call([command], shell=True)


def check_FID_devices():
    """Checks to see if a known FID USB device is currently connected. It does this by verifying if
    said device's SYMLINK (defined in /etc/udev/rules.d/50-usb-serial.rules) is present (active) in 
    the /dev Directory
    """

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
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
