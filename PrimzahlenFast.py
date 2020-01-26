ranges = 10000
zahlen = range(2,ranges,1)
primezahlen = 0
i = 2

while i < ranges:
    if zahlen[i - 2] == 0:
        i = i +1
        next
    print i
    a = 2 * i
    while a < ranges:
        zahlen[a - 2] = 0
        a = a + i
    i = i + 1
print zahlen
for i in zahlen:
    if i > 0:
        primezahlen = primezahlen + 1
print primezahlen