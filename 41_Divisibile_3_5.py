n = int(input('inserisci un numero: '))
if n%5 == 0 and n%3 == 0:
    print('il numero è divisibile sia per 3 che per 5')
elif n%5 == 0:
    print('il numero è divisibile per 5')
elif n%3 == 0:
    print('il numero è divisibile per 3')
else:
    print('il numero non è divisibile nè per 3 nè per 5')