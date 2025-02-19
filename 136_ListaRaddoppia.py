import random
l = []
for i in range(10):
    l.append(random.randint(1,100))
for i in range(len(l)):
    if not l[i]%2 == 0:
       l[i] = l[i]*2
print(l)