password = 'a123456'
x = 3
while x > 0:
	pwd = input('Password: ')
	if pwd == password:
		print('correct')
		break
	else:
		x = x - 1
		print('wrong, u have', x, 'time to try')