d1 = {'oggetto':'casa','prezzo':100000}
d2 = {'marchio':'Tatra','modello':'T813','trasmissione':'8x8','prezzo':230000}
for i in d2:
    if type(d2[i]) == str:
        d1[i] = d1.get(i, '' + d2[i])
    elif type(d2[i]) == int:
        d1[i] = d1.get(i, 0) + d2[i]
print(d1)