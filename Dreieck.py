import math

from tkinter import *

canvas_width = 500
canvas_height = 500
x = 0
y = 0
xa = 500
xb = 0
master = Tk()


leinwand = Canvas(master,
                  width=canvas_width,
                  height=canvas_height)
leinwand.pack()

for C in range(0, 500):
    x = C
    y = 2
    leinwand.create_line(x, y, x + 1, y + 1, fill="#000000")

for A in range(2 , 250):
    y = A
    leinwand.create_line(xa, y, xa + 1, y + 1, fill="#000000")
    xa = xa-1
    print (A)

for B in range(2 , 250):
    y = B
    leinwand.create_line(xb, y, xb + 1, y + 1, fill="#000000")
    xb = xb + 1

mainloop()