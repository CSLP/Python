year=eval(input())
if(year%4==0 and year%100!=0) or (year%4==0):
    print(year,":闰年")
else:
    print(year,"Not")
