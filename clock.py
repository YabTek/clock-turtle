import turtle
import time
trace=turtle.Turtle()
trace.hideturtle()
back_ground=turtle.Screen()
back_ground.bgcolor("black")
back_ground.setup(width=700,height=750)
back_ground.tracer(0)

def working_clock(hr,mn,sc,trace):
    trace.penup()
    trace.goto(0,0)
    trace.pensize(3)
    trace.pencolor("white")
    trace.speed(0)
    trace.pendown()
    trace.setheading(0)
    trace.circle(160)
  
    for i in range(12):
        trace.penup()
        trace.goto(0,160)
        trace.right(30)
        trace.forward(135)
        trace.pendown()
        trace.forward(25)

        
 #hour counter
    trace.penup()
    trace.goto(0,160)
    trace.pencolor("green")
    trace.setheading(90)
    trace.right((hr/12)*360)
    trace.pendown()
    trace.pensize(2)
    trace.forward(110)
 #minute counter
    trace.penup()
    trace.goto(0,160)
    trace.pensize(1)
    trace.pencolor("orange")
    trace.setheading(90)
    trace.right((mn/60)*360)
    trace.pendown()
    trace.pensize(1)
    trace.forward(86)
 #second counter
    trace.penup()
    trace.goto(0,160)
    trace.pencolor("pink")
    trace.setheading(90)
    trace.right((sc/60)*360)
    trace.pendown()
    trace.forward(64)

while True:
    hr=int(time.strftime("%I"))
    mn=int(time.strftime("%M"))
    sc=int(time.strftime("%S"))
    working_clock(hr,mn,sc,trace)
    
    back_ground.update()
    time.sleep(1)
      
    trace.clear()






                         
                         
    



