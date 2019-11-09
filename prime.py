
n=int(input("entre the value of n"))   #input taken by user

for i in range(2,n+1):                 #no. which are to be check
    
    c=int(0)                           #c is to be counted
    
    import math                        #to use sqrt func.
    
    x=math.sqrt(i)            
    for j in range(2,math.ceil         # i used a theorem in which { if a no.  in not devisible by all the numbers which are less or equal to squar root od that function thw the no.is prime}
    (x)+1):                            # j is the no.which will devide i    i used the theorem to reduse the loop
        
        if i%j==0:                     #checking remender
            
            c=c+1                      # increasing c depends on the no. of devisor 'i' have
            
            break                      # to break the loop if any divisor is caught 
            
    if c==0:                           # if c=0 then no. have no devisor thus its prime
        
        print(i)





