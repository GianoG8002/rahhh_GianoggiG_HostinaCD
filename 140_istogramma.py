n = int(input('inserire quanti valori sono necessari: '))
l = []
for i in range(n):
    l.append(int(input('inserire un valore: ')))
print()
print(' - - - - - - - - ')
print()
for i in l:
    for y in range(i):
        print('*', end='')
    print()
print()
print(' - - - - - - - - ')