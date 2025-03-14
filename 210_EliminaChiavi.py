k = input('inserire chiave da eliminare ')
d = {'marchio':'Tatra','modello':'T813','trasmissione':'8x8','prezzo':230000}
print('dizionario originale:',d)
if k in d:
    d.pop(k)
    print('chiave',k,'rimossa')
else:
    print('chiave non esistente nel dizionario')
print('dizionario aggiornato:',d)