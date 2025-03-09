p = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
l = []
i = 0
n = int(input('inserire u numero da 1 a 100 da scomporre: '))
o = n
while n>1:
    if n == 101:
        print('101 è un numero primo, ma io ho chiesto numeri solo fino a 100')
        quit()
    elif n>100:
        print("il numero è più grande dell'intervallo richiesto")
        quit()
    if n%p[i] == 0:
        l.append(p[i])
        n/=p[i]
    else:
        i+=1
if n<1:
    print("il numero è più piccolo dell'intervallo richiesto")
else:
    print('la lista dei fattori di',o,'è',l)