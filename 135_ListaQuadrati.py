import random
n = int(input('inserisci un numero: '))
l = []
for i in range(n):
    l.append(random.randint(1,20))
print(' - - - - - - - - - ')
print('numeri nella lista:')
for i in range(len(l)):
    print(l[i], end=' ')
print()
print(' - - - - - - - - - ')
print('numeri alla seconda nella lista:')
for i in range(len(l)):
    print(l[i]**2, end=' ')