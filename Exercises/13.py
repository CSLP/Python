from math import *
x=1
y=1
while x<=19:
	while y<=33:
		if(100-x-y)/3+x*5+y*3==100:
			print(x,y,100-x-y)
		y+=1
	y=1
	x+=1
for x in range(1,19):
	for y in range(1,33):
		if(100-x-y)/3+x*5+y*3==100:
			print(x,y,100-x-y)
