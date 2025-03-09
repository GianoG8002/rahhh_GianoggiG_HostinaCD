import random
listanum = []
n = int(input('inserire numero finale da 1 a 10: '))
i = 0
s = True
while len(listanum)<20:
    listanum.append(random.randint(1,10))
while s:
    if i<len(listanum) and listanum[i] != n:
        i+=1
    else:
        s = False
if i<len(listanum):
    print('ci sono',i,'numeri prima di',n,'nella lista')
else:
    print('non è stato trovato',n,'nella lista')