def scene_2(t, width, height, color):

    # Restablecer posición y transformación
    t.setpos(0, 0)
    t.setheading(0)

    # Dibujar el marco 1
    t.penup()
    t.setpos(-450, 335)
    t.pendown()
    t.color("black")
    for _ in range(2):
        t.forward(900)
        t.right(90)
        t.forward(500)
        t.right(90)

    # Dibujar el marco 2
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
    t.pendown
    t.color("aquamarine4")
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

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
    t.color(color)
    t.shapesize(5)
    t.setheading(90)
    t.shape("turtle")
    t.stamp()

    # Dibujo de tortuga

    t.penup()
    t.goto(100, -50)
    t.pendown()
    t.color(color)
    t.shapesize(4.7)
    t.setheading(90)
    t.shape("turtle")
    t.stamp()

# Dibujo de nombre de la tortuga

    t.penup()
    t.goto(100, 30)
    t.pendown()
    t.color("azure")
    t.write("Hola!", font=("Arial", 14, "bold"))


    # Dibujo de delfin
    def delfin():
        t.penup()
        t.goto(100, 120)
        t.pendown()
        t.color("LightBlue")
        t.shapesize(5, 1, 1)
        t.setheading(-45)
        t.shape("triangle")
        t.stamp()

        t.penup()
        t.goto(110, 100)
        t.pendown()
        t.color("LightBlue")
        t.shapesize(1, 3, 1)
        t.setheading(-65)
        t.shape("triangle")
        t.stamp()

        t.penup()
        t.goto(22, 110)
        t.pendown()
        t.color("LightBlue")
        t.shapesize(2, 4, 1)
        t.setheading(0)
        t.shape("square")
        t.stamp()

        t.penup()
        t.goto(40, 125)
        t.pendown()
        t.color("LightBlue")
        t.shapesize(6, 3, 1)
        t.setheading(260)
        t.shape("triangle")
        t.stamp()

        t.penup()
        t.goto(70, 122)
        t.pendown()
        t.color("LightBlue")
        t.shapesize(3.5, 2.8, 1)
        t.setheading(260)
        t.shape("triangle")
        t.stamp()

        t.penup()
        t.goto(-35, 120)
        t.pendown()
        t.color("LightBlue")
        t.shapesize(3.5, 2.9, 1)
        t.setheading(300)
        t.shape("triangle")
        t.stamp()

        t.goto(-10, 120)
        t.color("LightBlue")
        t.shapesize(2.5, 2.5, 1)
        t.setheading(90)
        t.shape("triangle")
        t.stamp()

        t.goto(-10, 155)
        t.color("LightBlue3")
        t.shapesize(2, 2, 1)
        t.setheading(90)
        t.shape("triangle")
        t.stamp()

        t.goto(20, 120)
        t.color("LightBlue3")
        t.shapesize(1, 2, 1)
        t.setheading(90)
        t.shape("triangle")
        t.stamp()

        t.goto(20, 100)
        t.color("LightBlue3")
        t.shapesize(1, 2, 1)
        t.setheading(270)
        t.shape("triangle")
        t.stamp()

        t.goto(-30, 120)
        t.color("black")
        t.shapesize(0.2)
        t.shape("circle")
        t.stamp()
        t.penup()

    delfin()

    # Dibujo de delfin
    def delfin_2():
        t.goto(-70, 160)
        t.color("LightBlue")
        t.shapesize(5, 1, 1)
        t.setheading(-45)
        t.shape("triangle")
        t.stamp()

        t.goto(-60, 140)
        t.color("LightBlue")
        t.shapesize(1, 3, 1)
        t.setheading(-65)
        t.shape("triangle")
        t.stamp()

        t.goto(-148, 150)
        t.color("LightBlue")
        t.shapesize(2, 4, 1)
        t.setheading(0)
        t.shape("square")
        t.stamp()

        t.goto(-130, 165)
        t.color("LightBlue")
        t.shapesize(6, 3, 1)
        t.setheading(260)
        t.shape("triangle")
        t.stamp()

        t.goto(-100, 162)
        t.color("LightBlue")
        t.shapesize(3.5, 2.8, 1)
        t.setheading(260)
        t.shape("triangle")
        t.stamp()

        t.goto(-205, 160)
        t.color("LightBlue")
        t.shapesize(3.5, 2.9, 1)
        t.setheading(300)
        t.shape("triangle")
        t.stamp()

        t.goto(-180, 160)
        t.color("LightBlue")
        t.shapesize(2.5, 2.5, 1)
        t.setheading(90)
        t.shape("triangle")
        t.stamp()

        t.goto(-180, 195)
        t.color("LightBlue3")
        t.shapesize(2, 2, 1)
        t.setheading(90)
        t.shape("triangle")
        t.stamp()

        t.goto(-150, 160)
        t.color("LightBlue3")
        t.shapesize(1, 2, 1)
        t.setheading(90)
        t.shape("triangle")
        t.stamp()

        t.goto(-150, 140)
        t.color("LightBlue3")
        t.shapesize(1, 2, 1)
        t.setheading(270)
        t.shape("triangle")
        t.stamp()

        t.goto(-200, 160)
        t.color("black")
        t.shapesize(0.2)
        t.shape("circle")
        t.stamp()

        t.goto(-140, 70)
        t.color("azure")
        t.write("Hola Marina!", font=("Arial", 14, "bold"))
        t.penup()
    delfin_2()

    # cuadrados (como los de bob esponja)
    # cuadrados 1

    t.goto(-350, -90)
    t.pendown()
    t.color("PaleGreen")
    t.shapesize(1)
    t.shape("square")
    t.stamp()

    t.penup()

    t.goto(-340, -80)
    t.pendown()
    t.color("LimeGreen")
    t.shapesize(1)
    t.shape("square")
    t.stamp()


    # cuadrados 2

    t.penup()

    t.goto(350, 90)
    t.pendown()
    t.color("PaleGreen")
    t.shapesize(1, 2, 4)
    t.shape("square")
    t.stamp()

    t.penup()

    t.goto(340, 80)
    t.pendown()
    t.color("LimeGreen")
    t.shapesize(1, 2, 4)
    t.shape("square")
    t.stamp()

    t.penup()