import math
date=int(input("entre the date  :"))
b=int(input("entre the month  :"))
year=int(input("entre the year  :"))
x=0
d=0
if date>=32:
    print("wrong date ")
if year%4==0:
    if b in range(1,3):
        r=(b-1)*31
    elif b in range(3,9):
        r=((b-1)*30) +(math.floor(b/2))-1
    elif b in range(9,13):
        r=((b-1)*30)+(math.floor((b+1)/2))-1  
    else:
        print('wrong month')
else:
    if b in range(1,3):
        r=(b-1)*31
    elif b in range(3,9):
        r=((b-1)*30) +(math.floor(b/2))-2
    elif b in range(9,13):
        r=((b-1)*30)+(math.floor((b+1)/2))-2 
    else:
        print ("wrong month")
print(r)        
        
for i in range(2000,year):
    if (i%4==0):
        a=366
    else:
        a=365
        
    x=x+a
print(x)
d=(date+r+x)%7
print(a+r+x)
print(d)
print(a)
if d==0:
    print("friday")
elif d==1:
    print("saturday")  
elif d==2:
    print("sunday")
elif d==3:
    print("monday")
elif d==4:
    print("tuesday")
elif d==5:
    print("wednesday")
elif d==6:
    print("thursday")    
    

