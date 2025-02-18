for i in range(1,11):
    for y in range(1,11):
        n = i*y
        if n<10:
            print(n, end='  ')
        else:
            print(n, end=' ')
    print()