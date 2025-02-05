numero = float(input('inserire il peso totale delle pesche: '))
costo = float(input('inserire il prezzo delle pesche al kilo: '))
prezzo = numero * costo
if prezzo > 10:
    prezzo = prezzo * .8
print('devi pagare', prezzo)