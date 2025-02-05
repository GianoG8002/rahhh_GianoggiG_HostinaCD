prezzo = 1.76
volume = float(input('inserisci il litraggio richiesto: '))
costo = volume * prezzo
if costo > 60:
    print('devi pagare', round(costo * .95, 2))
else:
    print('devi pagare', costo)