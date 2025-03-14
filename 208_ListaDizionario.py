d1 = {'nome':'libro','prezzo':3.50,'quantità':1000}
d2 = {'nome':'controller','prezzo':70,'quantità':60}
d3 = {'nome':'telefono','prezzo':800,'quantità':5}
l = [d1,d2,d3]
for i in l:
    i['prezzo totale'] = i.get('prezzo totale', i['prezzo'] * i['quantità'])
for i in l:
    for y in i:
        print(y + ': ' + str(i[y]) , end='   ')
    print('')
    print(' - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')