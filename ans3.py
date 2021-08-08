password = 'a123456'
x = 3
while x > 0:
	x = x - 1
	pwd = input('Password: ')
	if pwd == password:
		print('correct')
		break
	else:
		print('wrong, u have', x, 'time to try')