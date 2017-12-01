'''Prints out a Serial (tty) USB Device's product information.
Documentation for pyserial https://pythonhosted.org/pyserial/tools.html
'''
import os

from serial.tools.list_ports import comports

def main():
    usb_list = comports()

    for usb in usb_list:
        print('Device: ', usb.device)
        print('Location <bus>-<port>: ', usb.location)
        print('VID: ', usb.vid)
        print('PID: ', usb.pid)
        print('Serial #: ', usb.serial_number)
        print('Product String: ', usb.product)
        print('Manufacturer: ', usb.manufacturer, '\n')

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
