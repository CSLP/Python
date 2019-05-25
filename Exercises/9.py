while 1>0:
	x=eval(input())
	y=eval(input())
	a=x
	b=y
	while y>0:
		r=x%y
		x=y
		y=r
	print(x)
	print((a*b)/x)
