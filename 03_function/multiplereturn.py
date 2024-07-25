import math
def circle_status(radius):
    area=math.pi* radius*radius
    circumference=2*math.pi* radius
    return area ,circumference

a,c=circle_status(6)

print("Area ", a ,"Circumference", c)
    