def filtra_pari(lista):
    o = []
    for i in range(len(lista)):
        if lista[i]%2 == 1:
            o.append(lista[i])
    return o

n = int(input('inserire numero di valori da inserire nella lista: '))
l = []
for i in range(n):
    l.append(int(input('inserire un numero:')))
print(filtra_pari(l))