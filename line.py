import turtle
import random


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_line(p1, p2):
    # fill here
    draw_big_point(p1)
    draw_big_point(p2)
    x1, y1 = p1[0], p1[1] #(-100, -100)
    x2, y2 = p2[0], p2[1] #(300, 150)

    for i in range(0, 100, 5):
        t = i / 100

        x = (1-t)*x1 + t*x2 # 1-t:t의 비율로 x1, x2를 섞는다or더한다
        y = (1-t)*y1 + t*y2

        draw_point((x, y))

    draw_point(p2)


prepare_turtle_canvas()

# fill here
# points = [(-300, 200), (400, 350), (300, -300), (-200,-200)]
points = [(random.randint(-300, 300), random.randint(-300, 300)) for i in range(10)]

for p in points:
    draw_big_point(p)

for i in range(0,len(points) - 1):
    draw_line(points[i], points[i + 1])
draw_line(points[-1],points[0])

turtle.done()