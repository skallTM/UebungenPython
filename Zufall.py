import math

Rechenschieber = []

y = 0
null = 0
eins = 0
array = []

for x in range(0,24,1):
    Rechenschieber.append(0)
print Rechenschieber



for x in range(0,10000,1):
    Rechenschieber.insert(0, y)
    Rechenschieber.pop(23)
    x1 = Rechenschieber[19]
    x2 = Rechenschieber[20]
    x3 = Rechenschieber[22]
    x4 = Rechenschieber[23]
    end = Rechenschieber[23]
    Zahl = x1 ^ x2 ^ x3 ^ x4 ^ end ^ 1
    y = Zahl
    array.append(Zahl)
for x in array:
    if x == 0:
        null = null + 1
    else:
        eins = eins + 1
print eins
print null
print array