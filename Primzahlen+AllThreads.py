import threading
import time
primzahlen = []

def primzahle(start,stop):
    global primzahlen
    print "Start: %d ,Stop %d" % (start, stop)
    abbruch = False

    for i in range(start,stop,1):
        abbruch = False
        for a in range(2,i,1):
            if i % a == 0:
                abbruch = True
                break
        if abbruch == False:
            primzahlen.append(i)


for max in range(1, 6):
    millisStart = int(round(time.time() * 1000))
    threads = []
    for i in range(max):
        t = threading.Thread(target=primzahle ,args=(2+i*50000/max, (i+1)*50000/max+1))
        threads.append(t)
    for i in threads:
        i.start()
    for i in threads:
        i.join()
        print "stop"

    print len(primzahlen)
    millisEnd = int(round(time.time() * 1000))
    print "Time: %d " % ((millisEnd - millisStart) / 1000)