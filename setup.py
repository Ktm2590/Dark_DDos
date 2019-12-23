import os, sys
try:
	arg=sys.argv[1]
	if arg.lower()=="install":
		os.system("echo install package; apt install figlet wget git python -y &> log.txt; echo install modules; pip3 install -r requirements.txt &> log.txt")
	else:
		print('''
Не верный аргумент!
''')
except:
	print('''
Не верный аргумент!
''')
