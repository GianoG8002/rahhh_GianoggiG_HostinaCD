import random
n = int(input('inserire un numero: '))
o = 0
for i in range(n):
    r = random.randint(0,100)
    o = o + r
print(o)