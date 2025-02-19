import random
l = []
nd = 0
n = int(input('inserisci quanti numeri mettere nella lista: '))
for i in range(n):
    c = random.randint(1,20)
    l.append(c)
    if not c%2 == 0:
        nd+=1
print('la lista è:', l, 'e contiene', nd, 'numeri dispari')
