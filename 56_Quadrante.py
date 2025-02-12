x = float(input('inserire il valore della x: '))
y = float(input('inserire il valore della y: '))
if (x<=0 and y<=0) or (x>=0 and x>=0):
    print('il punto è nel primo o nel terzo quadrante')
else:
    print('il punto è nel secondo o nel quarto quadrante')
if (abs(x)==abs(y)):
    print('ed è sulla sua bisettrice')
else:
    print('ma non è sulla sua bisettrice')