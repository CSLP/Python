from math import *
n=1
s=0
x=eval(input())
while n:
	if x**(2*n-1)/factorial(2*n-1)<0.000001:
		break;
	s+=((-1)**(n+1))*(x**(2*n-1))/factorial(2*n-1)	
	n+=1
print(s)
print(sin(x))

print()
t=x
n=1
m=0.0
while abs(t)>=10e-6:
	m+=t
	t=-t*x*x/((n+1)*(n+2))
	n+=2
print(m)
