import random
l = []
for i in range(10):
    l.append(random.randint(0,100))
for i in range(len(l)):
    print(i, '=>', l[i])
print('- - - -')
for i in range(len(l)):
    print(i, '=>', l[-i-1])