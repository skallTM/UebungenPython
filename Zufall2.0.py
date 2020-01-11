import math
import threading
import time

v = 1
def fau ():
    global v
    s = v
    print (str(s) + " vorher")
    s = s + 1
    print (str(s) + " nacher")
    v = s

threads = []
for i in range(5):
    t = threading.Thread(target=fau)
    threads.append(t)
for i in threads:
    i.start()
for i in threads:
    i.join()

print v

