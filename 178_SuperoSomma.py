import random
listanum = []
n = int(input('inserire numero finale da 1 a 10: '))
i = 0
s = True
o = 0
while len(listanum)<20:
    listanum.append(random.randint(1,10))
while s:
    if i<len(listanum) and o<n:
        o+=listanum[i]
        i+=1
    else:
        s = False
if o>=n:
    print('serve sommare i primi',i,'numeri nella lista per raggiungere almeno',n)
else:
    print('non è stato possibile raggiungere',n,'con la somma dei numeri nella lista')