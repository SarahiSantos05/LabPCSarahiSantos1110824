def scene_1(t, width, height, color):

    # Dibujar el marco 1
    t.penup()
    t.setpos(-450, 335)  # Start from the top-left corner
    t.pendown()
    t.color("black")
    for _ in range(2):
        t.forward(900)  # Draw top and bottom sides of the frame
        t.right(90)
        t.forward(500)  # Draw right and left sides of the frame
        t.right(90)

    # Dibujar el marco 2
    t.penup()
    t.setpos(-450, 280)  # Start from the top-left corner
    t.pendown()
    t.color("black")
    for _ in range(2):
        t.forward(900)  # Draw top and bottom sides of the frame
        t.right(90)
        t.forward(600)  # Draw right and left sides of the frame
        t.right(90)

    #Diujar el oceano
    t.penup()
    t.setpos(-400, 250)
    t.pendown()
    t.color("aquamarine4")
    t.begin_fill()
    for _ in range(2):
        t.forward(width)  # Ajustar el ancho del océano
        t.right(90)
        t.forward(height)  # Dejamos un espacio para la arena
        t.right(90)
    t.end_fill()


    # Dibujar burbujas
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

    # Dibujar la tortuga
    t.penup()
    t.goto(100, -50)
    t.pendown()
    t.color("ForestGreen")
    t.shapesize(5)
    t.setheading(90)
    t.shape("turtle")
    t.stamp()

    t.penup()
    t.goto(100, -50)
    t.pendown()
    t.color("SpringGreen")
    t.shapesize(4.7)
    t.stamp()

    # Redactar el nombre de la tortuga
    t.penup()
    t.goto(100, 30)
    t.pendown()
    t.color("azure")
    t.write("Marina!", font=("Arial", 14, "bold"))

    # Draw fish
    t.penup()
    t.goto(-250, 120)
    t.pendown()
    t.color(color)
    t.shapesize(3, 2, 2)
    t.setheading(0)
    t.shape("triangle")
    t.stamp()

    t.penup()
    t.goto(-175, 125)
    t.pendown()
    t.color(color)
    t.shapesize(5, 1, 4)
    t.setheading(90)
    t.shape("triangle")
    t.stamp()

    t.penup()
    t.goto(-175, 110)
    t.pendown()
    t.color(color)
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

    # Draw second fish
    t.penup()
    t.goto(250, 150)
    t.pendown()
    t.color("MediumPurple3")
    t.shapesize(3, 2, 2)
    t.setheading(180)
    t.shape("triangle")
    t.stamp()

    t.penup()
    t.goto(175, 155)
    t.pendown()
    t.color("MediumPurple3")
    t.shapesize(5, 1, 4)
    t.setheading(90)
    t.shape("triangle")
    t.stamp()

    
    t.penup()
    t.goto(175, 140)
    t.pendown()
    t.color("MediumPurple3")
    t.shapesize(5, 1, 4)
    t.setheading(270)
    t.shape("triangle")
    t.stamp()

    t.penup()
    t.goto(150, 150)
    t.pendown()
    t.color("black")
    t.shapesize(0.2)
    t.shape("circle")
    t.stamp()

    t.penup()

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