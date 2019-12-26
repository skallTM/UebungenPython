from tkinter import *
import math


canvas_width = 500
canvas_height = 500

master = Tk()

def Verbindung(x1 ,y1, x2, y2):
    y = y1
    if x2 > x1 :
        steigung = y2 - y1 + 0.0
        breite = x2 - x1
        ersteSteigung = steigung / breite

        for A in range(x1, x2):
            x = A
            leinwand.create_line(x, y, x + 1, y + 1, fill="#000000")
            y = y + ersteSteigung
    else:
        Verbindung(x2, y2, x1, y1)

leinwand = Canvas(master,
                  width=canvas_width,
                  height=canvas_height)
leinwand.pack()


Verbindung(10, 10, 100, 47)
Verbindung(100, 47, 120, 70)
Verbindung(120, 70, 10, 10)

mainloop()
