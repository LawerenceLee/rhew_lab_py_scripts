#!/usr/bin/python
import subprocess 

# To run me from the command line simply type readtty.
# If permission is denied simply switch to root

usb_type = '' 

type_selection = raw_input("Select [A] ttyUSB, [B] ttyS ").upper() 
if type_selection == 'A':
	usb_type = 'USB'
elif type_selection == 'B':
	usb_type = 'S'

usb_port = raw_input("Specify port number: ")

add_or_not = raw_input("Would you like add additional arguments or use Valco template? [y/N/V] ").upper()
if add_or_not == 'Y':
	baud_rate = (raw_input('set baud rate (ex. 9600, 115200): '))

	set_parity  = raw_input("Parity choices [N] None, [E] Even, [O] Odd, [M] Mark, [S] Space : ").upper()
	parity = 'parity=PARITY_'
	if set_parity == 'N':
		parity += 'NONE'
	elif set_parity == 'E':
		parity += 'EVEN'
	elif set_parity == 'O':
		parity += 'ODD'
	elif set_parity == 'M':
		parity += 'MARK'
	elif set_parity == 'S':
		parity += 'SPACE'

	byte_size = 'bytesize='
	set_data_bits = raw_input('Data bit choices: 5, 6, 7, 8: ')
	if set_data_bits == '5':
		byte_size += 'FIVEBITS'
	elif set_data_bits == '6':
		byte_size += 'SIXBITS'
	elif set_data_bits == '7':
		byte_size += 'SEVENBITS'
	else:
		set_data_bits += 'EIGHTBITS'

	stop_bits = 'stopbits=STOPBITS_'
	set_stop_bits = raw_input('Stop Bit choices: 1, 1.5, 2, 3: ')
	if set_stop_bits == '1.5':
		stop_bits += 'ONE_POINT_FIVE'	
	elif set_stop_bits == '2':
		stop_bits += 'TWO'
	elif set_stop_bits == '3':
		stop_bits += 'THREE'
	else:
		stop_bits += 'ONE'
	
	xonxoff = 'xonxoff='
	set_xonxoff = raw_input("Enable software flow control [T/F]: ").upper()
	if set_xonxoff == 'T':
		xonxoff += 'True'
	else:
		xonxoff += 'False'
	
	
	rtscts = 'rtscts='
	set_rtscts = raw_input("Enable hardware (RTS/CTS) flow control [T/F]: ")
	if set_rtscts == 'T':
		rtscts += 'True'
	else:
		rtscts += 'False'

	dsrdtr = 'dsrdtr='
	set_dsrdtr = bool(raw_input("Enable hardware (DSR/DTR) flow control [T/F]: "))
	if set_dsrdtr == 'T':
		dsrdtr += 'True'
	else:
		dsrdtr += 'False'
elif add_or_not == "V":
	valco = True
else:
	print('Default settings used: 9600,8,N,1')


command = 'python -m serial.tools.miniterm /dev/tty{}{}'.format(usb_type, usb_port)

if add_or_not != 'Y':
	subprocess.call([command], shell=True)
elif valco == True:
	subprocess.call(['python -m serial.tools.miniterm /dev/ttyUSB0', '9600', 'parity=PARITY_NONE', 'stopbits=STOPBITS_ONE', 'xonxoff=False', 'rtscts=False', 'dsrdtr=False'], shell=True)
else:
	subprocess.call([command, baud_rate, parity, stop_bits, xonxoff, rtscts, dsrdtr], shell=True)

