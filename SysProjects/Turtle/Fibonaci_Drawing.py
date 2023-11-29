import turtle
import random
window = turtle.Screen()
window.setup(width=1200, height=800)
window.title("My New Drawing")
pen1 = turtle.Turtle(shape="classic")
# pen2 = turtle.Turtle(shape="classic")
pen1.pensize(2)
# pen1.hideturtle()
window.bgcolor("lightblue")


def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n ==2:
        return 1
    else:
        return (fib(n-2)+fib(n-1))

n = 20
ls = list()
for i in range(n):
    ls.append(fib(i))   

pen1.speed(0)
pen1.up()
pen1.forward(10)
pen1.left(90)
pen1.down()

color_list: list[int] = random.sample(range(111111, 999999), k=len(ls))
raito = 1
for index, width in enumerate(ls):
    # print(f'#{a[i-2]}')
    sqr = width * raito 
    pen1.color(f'#{color_list[i]}')
    pen1.begin_fill()
    for j in range(2):
        pen1.forward(sqr)
        pen1.left(90)
        pen1.forward(sqr)
        pen1.left(90)
        pen1.end_fill()
    pen1.up()
    pen1.forward(sqr)
    pen1.left(90)
    pen1.forward(sqr)
    pen1.down()

    
convas = turtle.getcanvas()
convas.postscript(file='01.png')
turtle.done()