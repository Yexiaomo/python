for i in range(1,10):
	for j in range(1,i+1):

		#print() 中添加 end='' 表示打印后不换行

		#print('%d*%d=%-2d ' % (j,i,i*j),end='')
		#或者这种格式化输出方式
		print('{}*{}={:2} '.format(j,i,i*j),end='')
	print()