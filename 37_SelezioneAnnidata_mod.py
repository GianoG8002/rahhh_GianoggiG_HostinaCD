print("Benvenuto nel mio programma di conversazione")
print()
risposta=input("Ti piace andare in bicicletta? Rispondi sì o no: ")
if risposta=="sì":
    print("Molto bene! Ti terrai in forma.")
    risposta = input("Ti piace anche il basket? ")
    if risposta=="sì":
        print("Allora sei un atleta!")
    else:
        print("Uno sport è meglio di niente!")
elif risposta == 'no':
    risposta = input("Ti piave un altro sport? Rispondi sì o no: ")
    if risposta == 'sì':
        print('Molto bene! Ti terrai in forma.')
    else:
        print('Non tutti sono sportivi.')
else:
    print('impara a leggere, ho chiesto sì o no')