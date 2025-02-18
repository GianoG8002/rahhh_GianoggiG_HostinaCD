n = 1
for i in range(1,12):
    if i%2 == 0:
        print('*')
    else:
        for y in range(n):
            print('*', end='')
        n+=1
        print()