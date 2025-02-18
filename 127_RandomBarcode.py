import random
n = int(input('inserire numero lanci di moneta: '))
for i in range(n):
    c = random.randint(0,1)
    if c == 0:
        print('|', end='')
    else:
        print(' ', end='')