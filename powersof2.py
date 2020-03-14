#draw a random integer x from range(1,8192)
#n count down from 13
#Is x equal to 0?
   #if yes: break
   #else: Is x bigger or equal to 2^n?
      #if not: n=n-1 
      #if yes: x=x-2^n n=n-1 
       
       
       
       
import random
x=random.randint(1,8193)
n=13
y=x
a=("")
while x!=0 and n>=1:   
    if x >= 2**n:
        x=x-2**n
        n=n-1
        a = a + "+"+"2**"+str(n)   
    else:
        n=n-1
print(str(y)+" "+"is"+" "+a[1:])


     
        