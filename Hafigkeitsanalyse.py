# -*- coding: utf-8 -*-
string = "my home is my castle"
alphabet = "abcdefghijklmnopqrstuvwxyz "
frequencies = dict()
Mo = ""
Liste = []
for i in string :
    frequencies[i] = frequencies.get(i, 0) + 1
print (frequencies)