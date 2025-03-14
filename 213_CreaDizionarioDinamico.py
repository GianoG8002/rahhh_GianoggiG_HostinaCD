n = int(input('inserire la lunghezza del: '))
d = {}
for i in range(n):
    s = input('inserire la chiave: ')
    d[s] = int(input('inserire il valore: '))
print('dizionario ordinato per valore:',dict(sorted(d.items(),key=lambda item: item[1], reverse=True)))