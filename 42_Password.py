p = input('inserire la password: ')
if p == 'PincoPallino2022':
    print('Password corretta!')
else:
    p = input('password errata, riprova: ')
    if p == 'PincoPallino2022':
        print('password corretta!')
    else:
        print('password errata, tentativi terminati')