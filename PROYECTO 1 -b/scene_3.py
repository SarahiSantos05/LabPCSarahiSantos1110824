
def scene_3(t, width, height, color):

    # Restablecer posición y transformación
    t.setpos(0, 0)
    t.setheading(0)

    # Dibjar marco 1
    t.penup()
    t.setpos(-450, 335)
    t.pendown()
    t.color("black")
    for _ in range(2):
        t.forward(900)
        t.right(90)
        t.forward(500)
        t.right(90)

    # Dibujar marco 2
    t.penup()
    t.setpos(-450, 280)
    t.pendown()
    t.color("black")
    for _ in range(2):
        t.forward(900)
        t.right(90)
        t.forward(600)
        t.right(90)


    # Dibujar el oceano
    t.penup()
    t.setpos(-400, 250)
    t.pendown()
    t.color("aquamarine4")
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

    # Dibujo de burbuja
    t.penup()
    t.goto(-100, 50)
    t.pendown()
    t.color("aquamarine")
    t.shapesize(2)
    t.shape("circle")
    t.stamp()

    t.penup()
    t.goto(-100, 50)
    t.pendown()
    t.color("azure")
    t.shapesize(1.2)
    t.shape("circle")
    t.stamp()

    # Dibujo de burbuja
    t.penup()
    t.goto(-90, 90)
    t.pendown()
    t.color("aquamarine")
    t.shapesize(1)
    t.shape("circle")
    t.stamp()

    t.penup()
    t.goto(-90, 90)
    t.pendown()
    t.color("azure")
    t.shapesize(0.6)
    t.shape("circle")
    t.stamp()

    # Dibujo de burbuja
    t.penup()
    t.goto(250, -50)
    t.pendown()
    t.color("aquamarine")
    t.shapesize(1)
    t.shape("circle")
    t.stamp()

    t.penup()
    t.goto(250, -50)
    t.pendown()
    t.color("azure")
    t.shapesize(0.2)
    t.shape("circle")
    t.stamp()

    # Dibujo de tortuga

    t.penup()
    t.goto(100, -50)
    t.pendown()
    t.color("ForestGreen")
    t.shapesize(5)
    t.setheading(150)
    t.shape("turtle")
    t.stamp()

    # Dibujo de tortuga
    t.penup()
    t.goto(100, -50)
    t.pendown()
    t.color("SpringGreen")
    t.shapesize(4.7)
    t.setheading(150)
    t.shape("turtle")
    t.stamp()


    # Dibujo de pez
    t.penup()
    t.goto(-250, 120)
    t.pendown()
    t.color("hotpink")
    t.shapesize(3, 2, 2)
    t.setheading(0)
    t.shape("triangle")
    t.stamp()

    t.penup()
    t.goto(-175, 125)
    t.pendown()
    t.color("hotpink")
    t.shapesize(5, 1, 4)
    t.setheading(90)
    t.shape("triangle")
    t.stamp()

    t.penup()
    t.goto(-175, 110)
    t.pendown()
    t.color("hotpink")
    t.shapesize(5, 1, 4)
    t.setheading(270)
    t.shape("triangle")
    t.stamp()

    t.penup()
    t.goto(-150, 120)
    t.pendown()
    t.color("black")
    t.shapesize(0.2)
    t.shape("circle")
    t.stamp()



    # Dibujo de segundo pez

    t.penup()
    t.goto(250, 0)
    t.pendown()
    t.color("SpringGreen")
    t.shapesize(3, 2, 2)
    t.setheading(180)
    t.shape("triangle")
    t.stamp()

    t.penup()
    t.goto(175, 5)
    t.pendown()
    t.color("SpringGreen")
    t.shapesize(5, 1, 4)
    t.setheading(90)
    t.shape("triangle")
    t.stamp()

    t.penup()
    t.goto(175, -10)
    t.pendown()
    t.color("SpringGreen")
    t.shapesize(5, 1, 4)
    t.setheading(270)
    t.shape("triangle")
    t.stamp()

    t.penup()
    t.goto(150, 0)
    t.pendown()
    t.color("black")
    t.shapesize(0.2)
    t.shape("circle")
    t.stamp()

    # Dibujo de tercer pez
    t.penup()
    t.goto(-250, 70)
    t.pendown()
    t.color(color)
    t.shapesize(3, 2, 2)
    t.setheading(0)
    t.shape("triangle")
    t.stamp()

    t.penup()
    t.goto(-175, 75)
    t.pendown()
    t.color(color)
    t.shapesize(5, 1, 4)
    t.setheading(90)
    t.shape("triangle")
    t.stamp()

    t.penup()
    t.goto(-175, 60)
    t.pendown()
    t.color(color)
    t.shapesize(5, 1, 4)
    t.setheading(270)
    t.shape("triangle")
    t.stamp()

    t.penup()
    t.goto(-150, 70)
    t.pendown()
    t.color("black")
    t.shapesize(0.2)
    t.shape("circle")
    t.stamp()

    #Dibujar algas

    t.penup()
    t.goto(-380, -100)
    t.pendown()
    t.color("green4")
    t.shapesize(0.5, 5, 1)
    t.shape("square")
    t.stamp()

    t.penup()
    t.goto(-350, -100)
    t.pendown()
    t.color("green3")
    t.shapesize(0.5, 4, 1)
    t.shape("square")
    t.stamp()

    t.goto(-320, -100)
    t.color("green2")
    t.shapesize(0.5, 5, 1)
    t.shape("square")
    t.stamp()

    t.goto(-310, -100)
    t.color("green3")
    t.shapesize(0.5, 3, 1)
    t.shape("square")
    t.stamp()

    t.goto(-280, -100)
    t.color("green")
    t.shapesize(0.5, 5, 1)
    t.shape("square")
    t.stamp()

    t.goto(-270, -100)
    t.color("green3")
    t.shapesize(0.5, 4.5, 1)
    t.shape("square")
    t.stamp()

    t.goto(-230, -100)
    t.color("green2")
    t.shapesize(0.5, 2, 1)
    t.shape("square")
    t.stamp()

    t.goto(-220, -100)
    t.color("green3")
    t.shapesize(0.5, 3.5, 1)
    t.shape("square")
    t.stamp()

    t.goto(-200, -100)
    t.color("green")
    t.shapesize(0.5, 5, 1)
    t.shape("square")
    t.stamp()

    t.goto(-180, -100)
    t.color("green3")
    t.shapesize(0.5, 5, 1)
    t.shape("square")
    t.stamp()

    t.goto(-160, -100)
    t.color("green")
    t.shapesize(0.5, 2.1, 1)
    t.shape("square")
    t.stamp()

    t.goto(-130, -100)
    t.color("green2")
    t.shapesize(0.5, 3.45, 1)
    t.shape("square")
    t.stamp()

    t.goto(-100, -100)
    t.color("green")
    t.shapesize(0.5, 5, 1)
    t.shape("square")
    t.stamp()

    t.goto(-90, -100)
    t.color("green2")
    t.shapesize(0.5, 4, 1)
    t.shape("square")
    t.stamp()

    t.goto(-70, -100)
    t.color("green3")
    t.shapesize(0.5, 3, 1)
    t.shape("square")
    t.stamp()

    t.goto(-60, -100)
    t.color("green2")
    t.shapesize(0.5, 2, 1)
    t.shape("square")
    t.stamp()

    t.goto(-40, -100)
    t.color("green3")
    t.shapesize(0.5, 1, 1)
    t.shape("square")
    t.stamp()

    t.goto(-20, -100)
    t.color("green2")
    t.shapesize(0.5, 4, 1)
    t.shape("square")
    t.stamp()

    t.goto(0, -100)
    t.color("green3")
    t.shapesize(0.5, 5, 1)
    t.shape("square")
    t.stamp()

    t.goto(0, -100)
    t.color("green4")
    t.shapesize(0.5, 5, 1)
    t.shape("square")
    t.stamp()

    t.goto(30, -100)
    t.color("green3")
    t.shapesize(0.5, 4, 1)
    t.shape("square")
    t.stamp()

    t.goto(60, -100)
    t.color("green2")
    t.shapesize(0.5, 5, 1)
    t.shape("square")
    t.stamp()

    t.goto(70, -100)
    t.color("green3")
    t.shapesize(0.5, 3, 1)
    t.shape("square")
    t.stamp()

    t.goto(100, -100)
    t.color("green")
    t.shapesize(0.5, 5, 1)
    t.shape("square")
    t.stamp()

    t.goto(110, -100)
    t.color("green3")
    t.shapesize(0.5, 4.5, 1)
    t.shape("square")
    t.stamp()

    t.goto(150, -100)
    t.color("green2")
    t.shapesize(0.5, 2, 1)
    t.shape("square")
    t.stamp()

    t.goto(160, -100)
    t.color("green3")
    t.shapesize(0.5, 3.5, 1)
    t.shape("square")
    t.stamp()

    t.goto(180, -100)
    t.color("green")
    t.shapesize(0.5, 5, 1)
    t.shape("square")
    t.stamp()

    t.goto(200, -100)
    t.color("green3")
    t.shapesize(0.5, 5, 1)
    t.shape("square")
    t.stamp()

    t.goto(220, -100)
    t.color("green")
    t.shapesize(0.5, 2.1, 1)
    t.shape("square")
    t.stamp()

    t.goto(250, -100)
    t.color("green2")
    t.shapesize(0.5, 3.45, 1)
    t.shape("square")
    t.stamp()

    t.goto(280, -100)
    t.color("green")
    t.shapesize(0.5, 5, 1)
    t.shape("square")
    t.stamp()

    t.goto(290, -100)
    t.color("green2")
    t.shapesize(0.5, 4, 1)
    t.shape("square")
    t.stamp()

    t.goto(310, -100)
    t.color("green3")
    t.shapesize(0.5, 3, 1)
    t.shape("square")
    t.stamp()

    t.goto(320, -100)
    t.color("green2")
    t.shapesize(0.5, 2, 1)
    t.shape("square")
    t.stamp()

    t.goto(340, -100)
    t.color("green3")
    t.shapesize(0.5, 1, 1)
    t.shape("square")
    t.stamp()

    t.goto(360, -100)
    t.color("green2")
    t.shapesize(0.5, 4, 1)
    t.shape("square")
    t.stamp()

    t.penup()
    t.goto(380, -100)
    t.pendown()
    t.color("green3")
    t.shapesize(0.5, 5, 1)
    t.shape("square")
    t.stamp()
    t.penup()
