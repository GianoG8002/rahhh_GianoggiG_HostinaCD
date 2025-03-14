s = input('inserire la stringa da dividere: ')
l = s.split()
o = {}
for i in l:
    o[i] = o.get(i,0)+1
print('dizionario stringa:',o)