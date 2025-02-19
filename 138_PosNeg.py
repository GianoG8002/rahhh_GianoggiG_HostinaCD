import random
lp = []
ln = []
n = int(input('inserisci un numero: '))
for i in range(n):
    c = random.randint(-20,20)
    if c > 0:
        lp.append(c)
    elif c < 0:
        ln.append(c)
print('numero magico positivo:', sum(lp))
print('numero magico negativo:', sum(ln))