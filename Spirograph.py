import turtle

turtle.bgcolor("black")
turtle.pensize(1.2)
turtle.speed(0)

for i in range(14):
    for colours in ["red","pink","cyan","blue","white","green","yellow","orange","grey"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(11)
        
turtle.hideturtle()



        
    
