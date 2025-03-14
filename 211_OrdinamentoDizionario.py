d = {1:'class 08', 4:'x4014', 3:'gp38', 2:'A4'}
print('dizionario ordinato per chiave:',dict(sorted(d.items())))
print('dizionario ordinato per valore:',dict(sorted(d.items(),key=lambda item: item[1])))