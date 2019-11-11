n=int(input("enter the no. of rows"))
for i in range (0,n):
    z=0
    j=0
    print('')    
    while z<i:
        z=z+1
        print(" " ,end="")
    for j in range (0,(2*(n-i))):
        if (j%2)!=0:
            print("*",end="")
        elif(j%2)==0:
            print(" ",end="")
            
