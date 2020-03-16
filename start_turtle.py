import turtle
kame = turtle.Turtle()
kame.shape('turtle')
kame.shapesize(2, 2, 3)
"""
#kame.forward(150)
#kame.circle(150)
#kame.undo()
kame.home()
kame.clear()
#w = kame.getscreen().window_width()
#h = kame.getscreen().window_height()
#p = kame.position()
#print(w, h, p)
#kame.goto(150, 200)
#d = kame.distance(0, 0)
#print(d)
kame.penup()
kame.circle(150)
"""
"""
kame.forward(200)
kame.left(120)
kame.forward(200)
kame.left(120)
kame.forward(200)
kame.left(120)
"""
"""
for i in range(3):
    kame.forward(200)
    kame.left(120)
"""
"""
for i in range(5):
    kame.forward(200)
    kame.left(144)
"""

import random
"""
while True:
    kame.left(random.randint(1, 360))
    kame.forward(15)
"""
"""
kame.penup()
kame.forward(200)
kame.left(90)
kame.pendown()
kame.circle(200)
kame.penup()
kame.home()
kame.pendown()
while kame.distance(0, 0) < 200:
    kame.left(random.randint(1, 360))
    kame.forward(15)
    if kame.distance(0, 0) > 200:
        kame.undo()
"""

for i in range(6):
    kame.left(60)
    kame.forward(120)
kame.penup()
kame.home()
