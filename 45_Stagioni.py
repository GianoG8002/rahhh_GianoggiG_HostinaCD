from datetime import datetime

def gAnno(g,m):
    date = datetime(1,m,g)
    return date.timetuple().tm_yday

g = int(input("numero giorno: "))
m = int(input("numero mese: "))
g = gAnno(g,m)
if g<80:
    print('è inverno')
elif g<172:
    print('è primavera')
elif g<182.5:
    print('è estate')
else:
    print('non esiste')