import math

Rechenschieber = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1]

y = 0
null = 0
eins = 0
array = []

for x in range(0,1000,1):
    Rechenschieber.insert(0, y)
    Rechenschieber.pop(10)
    x1 = Rechenschieber[4]
    x2 = Rechenschieber[7]
    end = Rechenschieber[9]
    Zahl = (x1 + x2 + end) % 2
    y = Zahl
    array.append(Zahl)
print array[60]
print array
for x in array:
    if x == 0:
        null = null + 1
    else:
        eins = eins + 1
print eins
print null