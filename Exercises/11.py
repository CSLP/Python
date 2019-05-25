from math import *
m=3
s=0
while m<101:
	k=int(sqrt(m))
	i=2
	while i<=k:
		if m%i==0:
			break
		i+=1
	else:
		print(m,end="  ")
		s+=m
	m+=2
print()
print(s)
