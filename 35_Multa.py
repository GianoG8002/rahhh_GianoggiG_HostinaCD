limit = int(input('inserisci il limite di velocità: '))
vel = int(input("inserire a che velocità l'auto sttava andando: "))
xtra = vel - limit
if xtra < 0:
    xtra = 0
    
if xtra == 0:
    print('stai guidando secondo i limiti')
elif xtra <= 10:
    print('devi pagare 36€ di multa')
elif xtra <= 40:
    print('devi pagare 148€ di multa')
elif xtra <= 60:
    print('devi pagare 370€ di multa')
elif xtra > 60:
    print('devi pagare 500€ di multa')