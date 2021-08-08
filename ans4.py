password = 'a123456'
x = 3
while x > 0:
	x = x - 1
	pwd = input('Password: ')
	if pwd == password:
		print('correct')
		break
	else:
		print('wrong')
		if x > 0:
			print('wrong, u have', x, 'time to try')
		else:
			print('no time to try la')