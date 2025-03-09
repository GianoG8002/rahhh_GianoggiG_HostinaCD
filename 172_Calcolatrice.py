n1 = 0
n2 = 0
o = ''
f = ''
while f.lower() != 'no':
    n1 = int(input('inserire il primo valore: '))
    n2 = int(input('inserire il secondo valore: '))
    print('addizione - sottrazione - moltiplicazione - divisione')
    o = input("inserire l'operazione richiesta: ")
    if o == 'addizione':
        print('risultato:',n1+n2)
        f = input('vuoi continuare? ')
    elif o == 'sottrazione':
        print('risultato:',n1-n2)
        f = input('vuoi continuare? ')
    elif o == 'moltiplicazione':
        print('risultato:',n1*n2)
        f = input('vuoi continuare? ')
    elif o == 'divisione':
        print('risultato:',n1/n2)
        f = input('vuoi continuare? ')
    else:
        input('operazione non trovata, riprova.')