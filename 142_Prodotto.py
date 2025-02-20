import random
import math
l = []
for i in range(10):
    l.append(random.randint(1,10))
print('il prodotto di 10 numeri da 1 a 10 è', math.prod(l))