import math

from tkinter import *

canvas_width = 1900
canvas_height =1500
x = 0
y = 10
xx = 1
yy = 10
pi = 3.141592653589793238462643383279502884197169399375105820974944592


master = Tk()

leinwand = Canvas(master,
                  width=canvas_width,
                  height=canvas_height)
leinwand.pack()

#w.create_oval(50,50,100,100)

for alpha in range(0, 360):
    x = math.cos((alpha/360.)*2*pi)*500+100
    y = math.sin((alpha/360.)*2*pi)*500+100
    leinwand.create_line(x, y, x+1, y+1, fill="#ff0000")
    print x
    print y



mainloop()

Hallo = 0
Hallo = math.sin(pi)
print Hallo