l1 = float(input('inserire il primo lato'))
l2 = float(input('inserire il secondo lato'))
l3 = float(input('inserire il terzo lato'))
if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l2 + l1):
  print('questi lati compongono un triangolo')
else:
  print('questi lati non possono comporre un triangolo')
