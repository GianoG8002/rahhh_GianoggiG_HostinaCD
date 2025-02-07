print('1 addizione - 2 sottrazione - 3 moltiplicazione - 4 divisione')
op = int(input('inserire operazione richiesta: '))
if op == 1:
    n1 = float(input('inserire addendo: '))
    n2 = float(input('inserire addendo: '))
    print('il risultato è', n1+n2)
elif op == 2:
    n1 = float(input('inserire minuendo: '))
    n2 = float(input('inserire sottraendo: '))
    print('il risultato è', n1-n2)
elif op == 3:
    n1 = float(input('inserire fattore: '))
    n2 = float(input('inserire fattore: '))
    print('il risultato è', n1*n2)
elif op == 4:
    n1 = float(input('inserire dividendo: '))
    n2 = float(input('inserire divisore: '))
    print('il risultato è', n1/n2)
else:
    print('operazione non inclusa nella lista')