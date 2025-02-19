import random
l = []
n = int(input('inserisci un numero: '))
for i in range(n):
    l.append(random.randint(1,20))
print('numero magico:', sum(l))