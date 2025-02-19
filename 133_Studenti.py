studenti = []
studenti_classe = ['Alex','Gabriele','Cristian','Davide','Loris']
for i in range(5):
    s = input('inserisci il nome di uno studente: ')
    if s in studenti_classe and s not in studenti:
        print('lo studente', s, 'è stato aggiunto')
        studenti.append(s)
    elif s in studenti_classe and s in studenti:
        print('questo studente non va inserito nella classe')
    else:
        print('studente non riconosciuto')
    print(' - - - - - - - - - - ')