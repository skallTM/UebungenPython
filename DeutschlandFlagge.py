import math

from tkinter import *

canvas_width = 750
canvas_height = 1500
rechts_oben_y = 398
links_unten_x = 148
master = Tk()
# def linien(startx, starty, endex, endey):
#     for linie in range()

leinwand = Canvas(master,
                  width=canvas_width,
                  height=canvas_height)
leinwand.pack()

# for linie1 in range(0, 498):
#     x = 2
#     y = linie1
#     leinwand.create_line(x, y, x+1 , y+1 , fill="#ff0000")
#
# for linie2 in range(0, 248):
#     x = linie2
#     y = 498
#     leinwand.create_line(x, y, x+1 , y+1 , fill="#ff0000")
#
# for linie3 in range(0, 498):
#     x = 248
#     y = linie3
#     leinwand.create_line(x, y, x+1 , y+1 , fill="#ff0000")
#
# for linie4 in range(0, 248):
#     x = linie4
#     y = 2
#     leinwand.create_line(x, y, x+1 , y+1 , fill="#ff0000")



for x in range(0, 750):
    for ausgemalt in range(0, 250):
        y = ausgemalt
        leinwand.create_line(x, y, x + 1, y + 1, fill="#000000")


for x in range(0, 750):
    for ausgemalt in range(250, 500):
        y = ausgemalt
        leinwand.create_line(x, y, x + 1, y + 1, fill="#FF0000")


for x in range(0, 750):
    for ausgemalt in range(500, 750):
        y = ausgemalt
        leinwand.create_line(x, y, x + 1, y + 1, fill="#FFFF00")



mainloop()