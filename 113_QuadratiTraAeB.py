n1 = int(input('inserire il numero di partenza: '))
n2 = int(input('inserire il numero finale: '))
print('i numeri alla seconda tra', n1, 'e', n2, 'sono: ')
for i in range(n1+1,n2):
    print(i**2, end=' ')