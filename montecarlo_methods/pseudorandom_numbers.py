from random import randrange, seed, random
import numpy as np
roll1 = randrange(1,7)
roll2 = randrange(1,7)
print (roll1, roll2)

N = 10**6
count = 0
for i in range (N):
    n1 = randrange(1,7)
    n2 = randrange(1,7)
    if n1 == 6 and n2 == 6:
        count += 1

print (count/N)

if random() < 0.2:
    print("Heads")
else:
    print("Tails")
