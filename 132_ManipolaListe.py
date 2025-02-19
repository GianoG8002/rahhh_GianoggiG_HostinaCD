studenti = ["Arianna","Bruno","Dario","Elena","Mario","Teresa"]
studenti.append('Gabriele')
studenti.append('Cristian')
studenti.insert(3,'Loris')
del(studenti[1])
studenti.remove('Teresa')
for i in range(len(studenti)):
    print(i, studenti[i])