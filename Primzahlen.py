primzahlen = []
abbruch = False

for i in range(2,50000,1):
    abbruch = False
    for a in range(2,i,1):
        if i % a == 0:
            abbruch = True
            break
    if abbruch == False:
        primzahlen.append(i)
print primzahlen
