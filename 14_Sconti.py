prezzo1 = float(input('inserisci il prezzo del primo paio di jeans: '))
prezzo2 = float(input('inserisci il prezzo del secondo paio di jeans: '))
prezzo_scontato1 = round(prezzo1 - prezzo1 * .2, 2)
prezzo_scontato2 = round(prezzo2 - prezzo2 * .2, 2)
prezzo = prezzo_scontato1 + prezzo_scontato2
print('il prezzo scontanto è:', prezzo)
contanti = int(input('inserisci i contanti: '))
resto = round(contanti - prezzo, 2)
print('resto:', resto)