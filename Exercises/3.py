from math import *
x=eval(input())
if x<0:
    y=abs(x)
elif x<15:
    y=exp(x)*cos(x)
elif x<30:
    y=x**5
else :
    y=(7+9*x)*log(x)
print(y)
