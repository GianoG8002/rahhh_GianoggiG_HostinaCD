import random
n1 = int(input('inserire un numero da 0 a 100: '))
n2 = int(input('inserire un altro numero da 0 a 100: '))
l = []
li = []
while len(li)<10:
    g = random.randint(0,100)
    l.append(g)
    if g <= max(n1,n2) and g >= min(n1,n2):
        li.append(g)
print('i numeri nel range inserito sono:',li)
print('sono stati stampati in totale',len(l),'numeri, di cui',len(li),'sono nel range richiesto')