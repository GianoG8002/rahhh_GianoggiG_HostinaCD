lista_numeri = []
risposta = ""
n = 0
while risposta.lower() != "no":
    lista_numeri.append(n**2)
    if risposta.lower() != "no":
        print('aggiunto il numero', n**2)
    risposta = input("Vuoi inserire altri numeri? ")
    n+=1
print(lista_numeri)