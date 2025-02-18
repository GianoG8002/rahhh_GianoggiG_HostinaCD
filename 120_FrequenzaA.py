f = input('inserisci una frase: ')
a = 0
for c in f:
    if c.lower()=='a':
        a = a+1
print('nella frase ci sono', a,'lettere A in totale')