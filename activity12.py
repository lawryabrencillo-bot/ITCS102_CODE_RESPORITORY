import getpass

username = 'lawry'
password = 'totatola08'

l = ( 'input username ---> ')

i = getpass.getpass ( 'input password ---> ')

if username == l and i == password :
     		print("access granted")

else :
	print("access denied")
