#!/usr/bin/python
import subprocess 

# To run me from the command line simply type readtty.
# If permission is denied simply switch to root

def main():
	"""
	readtty is a terminal program that helps construct
    Pyserial's miniterm (Mini-Terminal) command with many of its 
    special arguments such as baud rate, parity, bytesize, 
    and stop bits.
	"""
    
	tty_type = '' 
    
    # Choosing tty type of ttyUSB or ttyS
	type_selection = raw_input("Select [A] ttyUSB, [B] ttyS ").upper() 
	if type_selection == 'A':
		tty_type = 'USB'
	elif type_selection == 'B':
		tty_type = 'S'

    # Provide the port number
	usb_port = raw_input("Specify port number: ")

    # Main Command (Includes tty type, and port number)
	command = 'python -m serial.tools.miniterm /dev/tty{}{}'.format(tty_type, usb_port)

    # Adding additional arguments
	add_or_not = raw_input("Would you like add additional arguments or use a template? [y/N/T] ").upper()
	if add_or_not == 'Y':
        
        # Define Bits per second (Baud Rate)
		baud_rate = (raw_input('set baud rate (ex. 9600, 115200): '))

        # Set Parity
		set_parity  = raw_input("Parity choices [N] None, [E] Even, [O] Odd, [M] Mark, [S] Space : ").upper()
		parity = 'parity=PARITY_'
		if set_parity == 'E':
			parity += 'EVEN'
		elif set_parity == 'O':
			parity += 'ODD'
		elif set_parity == 'M':
			parity += 'MARK'
		elif set_parity == 'S':
			parity += 'SPACE'
		else:
			parity += 'NONE'

        # Choose byte size
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

        # Choose the number of Stop Bits
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

        # Enable software flow control
		xonxoff = 'xonxoff='
		set_xonxoff = raw_input("Enable software flow control [T/F]: ").upper()
		if set_xonxoff == 'T':
			xonxoff += 'True'
		else:
			xonxoff += 'False'
        
        # Enable hardware (RTS/CTS) flow control
		rtscts = 'rtscts='
		set_rtscts = raw_input("Enable hardware (RTS/CTS) flow control [T/F]: ")
		if set_rtscts == 'T':
			rtscts += 'True'
		else:
			rtscts += 'False'

        # Enable hardware (DSR/DTR) flow control
		dsrdtr = 'dsrdtr='
		set_dsrdtr = bool(raw_input("Enable hardware (DSR/DTR) flow control [T/F]: "))
		if set_dsrdtr == 'T':
			dsrdtr += 'True'
		else:
			dsrdtr += 'False'
        
        # Run command plus additional arguments defined above
		subprocess.call([command, baud_rate, parity, byte_size, stop_bits, xonxoff, rtscts, dsrdtr], shell=True)

	elif add_or_not == "T":
        
        # Choose from either the Vici Valco or Omega templates.
		template_choice = raw_input('Would you like the [V] Valco, or [O] Omega template? ').upper()
        
        # Valco
		if template_choice == 'V':
			subprocess.call([command, '9600', 'bytesize=EIGHTBITS', 'parity=PARITY_ODD', 'stopbits=STOPBITS_ONE', 'xonxoff=False', 'rtscts=False', 'dsrdtr=False'], shell=True)
		
        # Omega
        elif template_choice == 'O':
			subprocess.call([command, '9600',  'bytesize=EIGHTBITS', 'parity=PARITY_NONE', 'stopbits=STOPBITS_ONE', 'xonxoff=False', 'rtscts=False', 'dsrdtr=False'], shell=True)

	else:
        
        # Run command with default settings
		print('Default settings used: 9600,8,N,1')
		subprocess.call([command], shell=True)
        

if __name__ == "__main__":
    main()
