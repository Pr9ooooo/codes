import turtle
turtle.Screen().bgcolor("Red")
turtle.Screen().setup(500,300)
polygon=turtle.Turtle()
no_side=6
angle=360/no_side
for i in range(no_side): 
  polygon.forward(100)
  polygon.right(angle)
turtle.done()