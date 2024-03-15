from random import random

import points


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = Point(2, 3)
b = Point(7, 9)

print(f"a=({a.x},{a.y})")
print(f"a=({b.x},{b.y})")


#creating random 5 points

for _ in range(5):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    random_point = Point(x, y)
    points.append(random_point)