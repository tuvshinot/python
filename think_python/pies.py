import turtle
import math

draw = turtle.Turtle()


def triangle(t, height, top_angle):
    """ Draw triangle
    t : Turtle
    height : height of the triangle 
    top_angle : top angle of that triangle
    """
    side_length = height / math.cos(math.radians(top_angle / 2))
    bottom_length = height * math.sin(math.radians(top_angle / 2)) * 2
    t.lt(top_angle / 2)
    t.fd(side_length)
    t.rt(180 - (90 - top_angle / 2))
    t.fd(bottom_length)
    t.rt(180 - (90 - top_angle / 2))
    t.fd(side_length)
    t.rt(180 - top_angle / 2)

def pie(t ,segment_num, radius):
    turn_angle = 360.0 / segment_num

    
    for i in range(segment_num):
        triangle(t, radius, turn_angle)
        t.rt(turn_angle)


pie(draw, 10, 60)


turtle.mainloop()

