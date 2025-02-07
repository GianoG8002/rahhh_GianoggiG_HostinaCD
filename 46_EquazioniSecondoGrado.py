a = float(input('inserire il termine di secondo grado: '))
b = float(input('inserire il termine di primo grado: '))
c = float(input('inserire il termine noto: '))
if a!=0:
    delta = b**2 - 4*a*c
    if delta<0:
        print("l'equazione non ha soluzione")
    elif delta==0:
        res = round((-b+delta**.5)/(2*a), 2)
        print("la soluzione dell'equazione è:", res)
    else:
        res1 = round((-b+delta**.5)/(2*a), 2)
        res2 = round((-b-delta**.5)/(2*a), 2)
        print("le soluzioni dell'equazione sono:", res1, 'e', res2)
else:
    print("il risultato dell'equazione è:", round((-c)/b), 2)