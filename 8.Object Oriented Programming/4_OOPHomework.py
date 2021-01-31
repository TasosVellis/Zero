import math
# Problem 1
#
# Fill in the Line class methods to accept coordinates as a
# pair of tuples and return the slope and distance of the line.
class Line:
    """
    coordinate1 = (3,2)
    coordinate2 = (8,10)
    li = Line(coordinate1,coordinate2)
    li.distance() = 9.433981132056603
    li.slope() = 1.6
    distance formula = square((x2-x1)^2 + (y2-y1)^2)
    slope formula = y2-y1 / x2-x1
    """
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)
li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())
# Problem 2
#
# Fill in the class


class Cylinder:
    """
    c = Cylinder(2,3)
    c.volume() = 56.52
    c.surface_area() = 94.2
    """
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.pi * self.radius ** 2 * self.height

    def surface_area(self):
        top_bottom = 2 * self.pi * self.radius**2
        return top_bottom + 2 * self.pi * self.radius * self.height


c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())
