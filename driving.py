driving = input('請問有沒有開過車?')
age = input('請問年齡是?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測試')
	else:
		print('奇怪怎麼可以開車')
elif driving == '沒有':
	if age >= 18:
		print('你可以去考駕照')
	else:
		print('再幾年就可以考駕照')
else:
	print('只能輸入有或沒有')