Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle.Pen()
tao.shape('turtle')

def Star():
    tao.left(36)
    tao.forward(100)
    tao.left(144)
    tao.forward(100)
    tao.left(144)
    tao.forward(100)
    tao.left(144)
    tao.forward(100)
    tao.left(144)
    tao.forward(100)
    tao.left(108)

    
def Goto(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

    
Goto(152,158)
Star()
Goto(-152,144)
Star()
