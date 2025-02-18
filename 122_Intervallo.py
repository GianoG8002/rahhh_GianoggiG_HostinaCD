a = int(input('inserire il numero di partenza: '))
b = int(input('inserire il numero finale: '))
r = 0
if a>b:
    print('il valore del numero finale non può essere maggiore del numero iniziale')
else:
    for i in range(a,b+1):
        r = r+i
print('la somma dei numeri da', a, 'e', b, 'è', r)