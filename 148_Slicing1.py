i = input('inserire una stringa di almeno 4 caratteri: ')
if len(i)<4:
    print('caratteri insufficenti')
else:
    print(i[1:4])