# Rhew Lab Scripts
Python scripts used to identify, adjust permissions, and read serial communications from USB devices.

## Terminal Commands 
- `seeserial.py`
  * Shows all currently connected USB devices (except Memory Storage Devices like Flash Drives), along with various attributes
  of each device.
  * Checks to see if a known FID USB device is currently connected. It does this by verifying if
    said device's SYMLINK (defined in /etc/udev/rules.d/50-usb-serial.rules) is present (active) in 
    the /dev Directory.
- `unlocktty.py`
  * Grants all users permission to read and write from all USBtty ports currently connected.
- `readtty.py`
  * Reads a user provided USBtty port and then allows for arguments to be added such as bits per second (baud), parity, data bits, and stop bits.
- `seeUSBserial.py`
  * Does much the same thing as `seeserial` in regards to showing all USB devices that are currently connected, but can be easily modified to change what attributes are shown (see [pyserial DOCS](https://pythonhosted.org/pyserial/tools.html))
