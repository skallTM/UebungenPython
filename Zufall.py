import math

Rechenschieber = [0, 1, 0, 1, 1, 0, 1, 0, 0]

y = 0
array = []

for x in range(0,100,1):
    Rechenschieber.insert(0, y)
    Rechenschieber.pop(9)
    x1 = Rechenschieber[4]
    x2 = Rechenschieber[7]
    end = Rechenschieber[8]
    Zahl = (x1 + x2 + end) % 2
    y = Zahl
    array.append(Zahl)
print array[60]
print array