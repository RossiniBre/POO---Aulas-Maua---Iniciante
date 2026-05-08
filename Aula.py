import turtle

t = turtle.Turtle()
t.speed(3)

raio = 40
comprimento = 150

# ----- círculos -----

# círculo de baixo
t.penup()
t.goto(0, -raio)
t.pendown()
t.circle(raio)

# círculo de cima
t.penup()
t.goto(0, raio)
t.pendown()
t.circle(raio)

# ----- linhas -----

# linha de cima
t.penup()
t.goto(raio, raio * 2)
t.setheading(0)
t.pendown()
t.forward(comprimento)

# linha de baixo
t.penup()
t.goto(raio, 0)
t.setheading(0)
t.pendown()
t.forward(comprimento)

# ----- curva correta (fechando certinho) -----

# começa NO FINAL da linha de cima
t.penup()
t.goto(raio + comprimento, raio * 2)
t.setheading(0)
t.pendown()

# faz um quarto de curva pra baixo
t.circle(-raio, 90)

# depois outro quarto pra fechar embaixo
t.circle(-raio, 90)
t.right(90)
t.forward(80)

turtle.done()