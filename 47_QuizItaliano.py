print("Ciao! Facciamo un quiz.")
risposta = int(input("In che anno è nato Alessandro Manzoni?"))
if risposta > 1785:
    print("Uhm… è nato prima dell’anno",risposta)
    risposta2 = input("Vuoi studiare di più? Rispondi sì o no")
    if risposta2== "sì":
        print("Ottimo.")
    else:
        print("Ti conviene farlo ugualmente.")
elif risposta < 1785 :
    print("Uhm… è nato dopo dell’anno",risposta)
else:
    print("Bene. Hai inserito l’anno corretto.")
    print("Chi sono i due protagonisti dei Promessi Sposi?")
    n1 = input('inserisci il primo protagonista: ')
    n2 = input('inserisci il secondo protagonista: ')
    if n1 == ('Lorenzo' or 'Lucia') and n2 == ('Lorenzo' or 'Lucia'):
        print('bene, hai inserito i protagonisti correti!')
    elif n1 == ('Lorenzo' or 'Lucia') or n2 == ('Lorenzo' or 'Lucia'):
        print('ne hai azzeccato solo uno, cerca di fare di meglio')
    else:
        print('hai sbagliato entrambi, male!')