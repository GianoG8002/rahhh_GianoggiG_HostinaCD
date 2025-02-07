n = int(input('inserire numero di articoli: '))
p = float(input('inserire prezzo individuale degli articoli: '))
c = p*n
if n<10:
    if c<10:
        print('inporto da inserire:', c*.98)
    else:
        print('importo da inserire:', c*.95)
elif n==10:
    print('importo da inserire:', c*.9)
else:
    if c<100:
        print('importo da inserire:', c*.7)
    elif c>100:
        print('importo da inserire:', c*.5)
    else:
        print('importo da inserrie:', c*.65)