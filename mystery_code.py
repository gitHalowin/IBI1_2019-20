# What does this piece of code do?
# Answer: draw random integers until the first prime number or 1 is drawn

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

#make a condition for while loop
p=False
while p==False:
    p=True
    n = randint(1,100)
    u = ceil(n**(0.5))
    for i in range(2,u+1):
        if n%i == 0:
            #draw another integer
            p=False


     
print(n)
