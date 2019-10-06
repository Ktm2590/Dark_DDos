import os
import time
import requests
import sys
from termcolor import colored, cprint
import filecmp

os.system("mkdir update_check")
os.system("cd update_check && wget https://raw.githubusercontent.com/DarkGa/Dark_DDos/master/ver.txt &> log.txt")
update = filecmp.cmp('../Dark_DDos/ver.txt', '../Dark_DDos/update_check/ver.txt')
os.system("cd ../Dark_DDos")
os.system("rm -rf update_check")
if update == True:
	pass
if update == False:
	print("detect new version!")
	os.system("cp update.py ../")
	os.system("cd ../ && python3 update.py")
	