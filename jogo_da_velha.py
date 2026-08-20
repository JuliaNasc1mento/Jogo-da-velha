from turtle import Turtle, onscreenclick, mainloop, onkey, listen
turtle = Turtle ()
turtle.speed(0)

#desenhar tabuleiro
turtle.penup()
turtle.pensize(4)
turtle.goto(50, 150)
turtle.pendown()
turtle.right(90)
turtle.forward(300)

turtle.penup()
turtle.goto(-50, 150)
turtle.pendown()
turtle.forward(300)

turtle.penup()
turtle.goto(-150, 50)
turtle.pendown()
turtle.left(90)
turtle.forward(300)

turtle.penup()
turtle.goto(-150, -50)
turtle.pendown()
turtle.forward(300)

#centralização
def posicao(x, y):
    turtle.penup()
    turtle.goto(x - (x % 100) + 100, y - (y % 100) + 100)
    turtle.pendown()
   
#desenhar xis
def xis():
    turtle.pendown()
    turtle.pensize(4)
    turtle.pencolor("blue")
    turtle.left(45)
    turtle.forward(45)
    turtle.left(180)
    turtle.forward(90)
    turtle.forward(-45)
    turtle.left(90)
    turtle.forward(45)
    turtle.left(180)
    turtle.forward(90)
    turtle.left(360/1.6)

#desenhar circulo
def circulo():
    turtle.penup()
    y_atual = turtle.ycor()
    novo_y = y_atual - 40
    turtle.sety(novo_y)
    turtle.pendown()
    turtle.pensize(4)
    turtle.pencolor("red")
    turtle.circle(40)

#altenancia entre X e O
onscreenclick(posicao)
onkey(xis, "x")
listen()
onkey(circulo, "o")
listen()
onkey(xis, "1")
listen()
onkey(circulo, "2")
listen()

mainloop()