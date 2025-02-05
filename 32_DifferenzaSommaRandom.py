import random
n1 = random.randint(0,10)
n2 = random.randint(0,10)
print('primo numero:', n1, '- secondo numero:', n2)
if n1*n2 > 20:
    print(str(max(n1,n2)), 'meno', str(min(n1,n2)), 'fa', str(max(n1,n2)-min(n1,n2)))
else:
    print(str(max(n1,n2)), 'più', str(min(n1,n2)), 'fa', str(n1+n2))