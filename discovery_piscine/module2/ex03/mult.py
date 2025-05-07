f_num = int(input('Enter the first number:'))
s_num = int(input('Enter the second number:'))
mult = f_num * s_num

print(('%i x %i = %i') % (f_num, s_num, mult))

if (mult > 0):
	print('The result is positive.')
elif (mult < 0):
	print('The result is negative.')
else:
	print('The result is positive and negative.')
