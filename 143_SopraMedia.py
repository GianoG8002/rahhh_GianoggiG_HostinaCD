import random
l = []
for i in range(10):
    l.append(random.randint(1,10))
m = sum(l)/len(l)
n = 0
for i in range(10):
    if l[i]>m:
        n+=1
print('ci sono', n, 'termini sopra la media nella lista')