'''sum=0
x=100
while(x>=100 and x<=200):
    sum=sum+x
    x+=2
print(sum)'''
# import module
'''import turtle
from random import randint, choice

# set up screen
width = 700
height = 500
S = turtle.Screen()
S.setup(width,height)
S.bgcolor('black')
S.title("Fireworks")

# colors
colors =['red','green','yellow','gold','pink','cyan','white','orange',
         'violet','coral']

class Fireworks:
    def init(self,radius):
        self.T = turtle.Pen()
        self.T.speed(0)
        self.T.color(choice(colors))
        self.T.hideturtle()
        self.T.up()
        self.T.setposition(randint(-250,250),randint(0,200))
        self.T.down()
        self.radius = radius

    def update(self):
        self.T.forward(self.radius)
        self.T.backward(self.radius)
        self.T.left(10)

    def clean(self):
        self.T.clear()
        self.T.color(choice(colors))
        self.T.up()
        self.T.setposition(randint(-250,250),randint(0,200))
        self.T.down()       

# Objects
T1 = Fireworks(randint(10,100))
T2 = Fireworks(randint(10,100))
T3 = Fireworks(randint(10,100))
T4 = Fireworks(randint(10,100))
T5 = Fireworks(randint(10,100))
T6 = Fireworks(randint(10,100))
T7 = Fireworks(randint(10,100))
   

T = turtle.Pen()
T.sety(-150)
T.color('gold')
T.write('Happy New Year  2023 !',align='center',font=(None,40))
T.hideturtle()

while True:
       
    for i in range(36):
        T1.update()
        T2.update()
        T3.update()
        T4.update()       
        T5.update()
        T6.update()
        T7.update()
       
    T1.clean()
    T2.clean()
    T3.clean()
    T4.clean()  
    T5.clean()
    T6.clean()
    T7.clean()

turtle.mainloop()

import turtle
skk = turtle.Turtle()
 
for i in range(4):
    skk.forward(50)
    skk.right(90)
     
turtle.done()

import turtle   #Outside_In
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
skk = turtle.Turtle()
skk.color("blue")
 
def sqrfunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(90)
        size = size-5
 
sqrfunc(146)
sqrfunc(126)
sqrfunc(106)
sqrfunc(86)
sqrfunc(66)
sqrfunc(46)
sqrfunc(26)

import turtle   #Outside_In
import turtle
import time
import random
 
print ("This program draws shapes based on the number you enter in a uniform pattern.")
num_str = input("Enter the side number of the shape you want to draw: ")
if num_str.isdigit():
    squares = int(num_str)
 
angle = 180 - 180*(squares-2)/squares
 
turtle.up
 
x = 0
y = 0
turtle.setpos(x, y)
 
 
numshapes = 8
for x in range(numshapes):
    turtle.color(random.random(), random.random(), random.random())
    x += 5
    y += 5
    turtle.forward(x)
    turtle.left(y)
    for i in range(squares):
        turtle.begin_fill()
        turtle.down()
        turtle.forward(40)
        turtle.left(angle)
        turtle.forward(40)
        print (turtle.pos())
        turtle.up()
        turtle.end_fill()
 
time.sleep(11)
turtle.bye()'''

import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(36000):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)

