#!/usr/bin/python
# This script grants all permissions to all users (e.g crwxrwxrwx) for all ttyUSB devices currently connected.
# To EXECUTE simply type "unlocktty" into the command prompt.


import os
import stat

def grant_permissions():
	"""
	This script grants all permissions to all users
	(e.g crwxrwxrwx) for all ttyUSB devices currently connected.
	"""
	for num in range(16):
		try:
			path = "/dev/ttyUSB{}".format(num)	
			os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
		except Exception as e:
			#print(e)
			pass
		else:
			print("[+] ttyUSB{} was granted all permissions.".format(num))

if __name__ == "__main__":
	grant_permissions()
