
import turtle
import time
t=turtle.Pen()
t.speed(100)
colors=["red","yellow","blue","green"]
for x in range(0,100,1):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(61)
    t.width(x/20)
time.sleep(10)