password = input('Password (3 time only): ')
x = 3
while password == 'a123456':
	print('correct')
	break
while password != 'a123456':
	x = x - 1
	if x == 0:
		print('bye')
		break
	print('wrong', x)
	password = input('Password: ')
	if password == 'a123456':
		print('correct')
		break