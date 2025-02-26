import random
import math
n = input('inserire il proprio nome: ')
print('password:',(n[:math.floor(len(n)/2)]+str(random.randint(0,9))+str(random.randint(0,9))+n[math.floor(len(n)/2):]))