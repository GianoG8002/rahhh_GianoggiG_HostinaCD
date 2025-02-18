print('Le coppie di numeri che ottengono 20 quando moltiplicati sono', end=': ')
for i in range(1,21):
    for y in range(1,21):
        if i*y == 20:
            print(i, 'x', y, end=' , ')