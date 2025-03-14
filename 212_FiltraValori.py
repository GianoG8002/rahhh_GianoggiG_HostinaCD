d = {'class 08':32, 'x4014':130, 'gp38':105, 'A4':203}
m = sum(d.values())/len(d.values())
print('chiavi con valori maggiori alla media:',end=' ')
for i in d:
    if d[i] > m:
        print(i+': '+str(d[i]),end=', ')