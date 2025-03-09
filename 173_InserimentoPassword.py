print()
p = 'Helldiver69'
i = ''
e = 0
while e<3:
    print('Accedi')
    if e==0:
        print()
    else:
        print('Tentativi rimanenti:',3-e)
        print('Password errata, riprova.')
    i = input('Password: ')
    print()
    print(' - - - - - - - ')
    print()
    if i == p:
        print('Bentornato')
        quit()
    else:
        e+=1
print('Tentativi esauriti, riprova più tardi')