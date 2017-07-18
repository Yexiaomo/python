sum = 0
tmp = 1
'''上面可以写成一行
sum, tmp = 0, 1
'''
for i in range(1,11):
	tmp = 1
	for j in range(1,i+1):
		tmp *= j
	sum += tmp;
print('1!+2!+...+10! =',sum)