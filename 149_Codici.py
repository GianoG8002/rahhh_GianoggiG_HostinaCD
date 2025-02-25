c = ['AFCDDR-CF-2020', 'SEDTYR-XC-2019']
for i in range(len(c)):
    s = c[i]
    if s[-4:] == '2020':
        print('il codice', c[i], 'finisce con 2020')