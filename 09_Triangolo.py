import math
base = int(input('inserisci il lato: '))
altezza = math.floor((base**2-(base/2)**2)**0.5)
area = (base * altezza) / 2
perimetro = 3 * base
print('area:',area,'- perimetro:',perimetro)