import random
listanum = []
listapari = []
n = int(input('inserire numero valori pari: '))
i = 0
while len(listanum)<20:
    listanum.append(random.randint(1,100))
while len(listapari)<n and i<20:
    if listanum[i]%2 == 0:
        listapari.append(listanum[i])
    i+=1
print('listapari:',listapari)