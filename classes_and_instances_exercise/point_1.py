from math import sqrt


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, new_x: int):
        self.x = new_x

    def set_y(self, new_y: int):
        self.y = new_y

    def distance(self, other_x: int, other_y: int):
        result = sqrt(((self.x - other_x) ** 2) + ((self.y - other_y) ** 2))
        return result


p: Point = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))
