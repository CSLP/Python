a=0
b=1
i=2
print(a,end='\t')
print(b,end='\t')
while i<20:
	c=a+b
	a=b
	b=c
	if (i+1)%5==0:
		print(c,end='\n')
	else :
		print(c,end='\t')
	i+=1
print()
a,b=0,1
i=0
while i<20:
	if (i+1)%5==0:
		print(a,end='\n')
	else :
		print(a,end='\t')
	a,b=b,a+b
	i+=1
a,b=0,1
i=0
while i<10:
	if(i+1)%3==0:
		print(a,'\t',b,end='\n')
	else:
		print(a,'\t',b,end='\t')
	a,b=a+b,a+b+b
	i+=1
	
