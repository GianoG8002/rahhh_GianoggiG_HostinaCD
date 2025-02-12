a = int(input('inserire anno: '))
if not(a%100 and a%400 != 0) and a%4 == 0:
    print("l'anno è bisestile")
else:
    print("l'anno è civile")