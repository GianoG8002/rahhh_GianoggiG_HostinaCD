biglietto = 30
prezzo = int(input('inserire prezzo camera: '))
durata = int(input('inserire durata permanenza: '))
costo = biglietto + prezzo * durata
print('il prezzo totale per il viaggio è di ' + str(costo))