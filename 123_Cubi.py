n = int(input('inserire un numero: '))
print('i cubi interi minori o uguali a', n, 'sono:', end=' ')
for i in range(1,n+1):
    if i**3 <= n:
        print(i**3, end=' ')