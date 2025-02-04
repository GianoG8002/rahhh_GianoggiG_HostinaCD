print("inserire prezzo pesche al pezzo")
prezzo = float(input())
print("inserire peso delle pesche acquistate")
peso = float(input())
totale = prezzo * peso
print("devi pagare",totale,"euro")
print("inserire importo banconota")
banconota = int(input())
resto = banconota - totale
print("Otterrai di resto ",resto,"euro")