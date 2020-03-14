#
# Repeat
    draw a random integer j from range(1,100)
    #Does j equal to 1?
    #if not:
       #if j is even: divide j by 2
       #if j is odd: multiply j by 3 and add 1
    #if yes:
    #break


"""

import random
j=random.randint(1,100)
while j!=1:
    if j%2==0:
        j=j/2
        print(j)
    else:
        j=3*j+1
        print(j)
        
    
 
       