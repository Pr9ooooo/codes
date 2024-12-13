import turtle
m=turtle.Screen()
turtle.speed(11)
m.bgcolor("black")
m.title("Colour Mania")
m_pen=turtle.Turtle()
colors=["green","blue","red","yellow","pink","orange"]

for x in range(360):
    m_pen.pencolor(colors[x % 6])
    m_pen.width(x/100 + 1)
    m_pen.forward(x)
    m_pen.left(60)







