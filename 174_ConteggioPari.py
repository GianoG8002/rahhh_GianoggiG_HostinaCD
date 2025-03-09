import random
n = int(input('inserire un numero: '))
l = []
t = 0
while len(l)<n:
    g = random.randint(40,90)
    if g%2 == 0:
        l.append(g)
    t+=1
print('numeri totali generati:',t)