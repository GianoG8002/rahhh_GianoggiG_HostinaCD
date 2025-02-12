m = int(input('inserisci il numero del mese: '))
if m == 2:
    print('il mese dura 28 giorni')
elif m == 4 or m == 6 or m == 9 or m == 10:
    print('il mese dura 30 giorni')
else:
    print('il mese dura 31 giorni')