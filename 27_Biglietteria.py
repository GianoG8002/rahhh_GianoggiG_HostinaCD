prezzo = float(input('inserisci il prezzo del biglietto '))
numero = int(input('inserisci il numero di biglietti acquistati '))
x = numero
while x > 20:
    numero = numero - 1
    x = x - 20
totale = numero * prezzo
print('il totale da pagare è', totale)