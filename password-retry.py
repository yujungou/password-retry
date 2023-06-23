password = 'a123456'
i = 3
while i > 0:
	pwd = input('Please enter the password: ')
	if pwd == password:
		print('pass')
		break
	else:
		i = i - 1
		print('Wrong! You still have', i, 'chance')