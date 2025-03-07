import random
n = random.randint(1,100)
g = 0
print(n)
while g != n:
    g = int(input('Indovina il numero: '))
    if g == n:
        print('godo, è quello giusto')
    elif g < n:
        print('pezzente, quello giusto è maggiore')
    elif g > n:
        print('pezzente, quello giusto è minore')