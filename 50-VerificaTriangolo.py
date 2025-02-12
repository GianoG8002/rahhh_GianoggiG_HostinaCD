lato1 = float(input("inserire primo lato "))
lato2 = float(input("inserire secondo lato "))
lato3 = float(input("inserire terzo lato "))
if lato1 == lato2 and lato2 == lato3:
  print("il triangolo è equilatero")
elif lato1 == lato2 or lato2 == lato3 or lato1 == lato3:
  print('il triangolo è isoscele')
else:
  print("il triangolo è scaleno")
