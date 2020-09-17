from random import uniform
from math import sqrt
x_min, x_max = -1, 1
y_min, y_max = -1, 1

def random_point2D():
    return [uniform(x_min, x_max), uniform(y_min,y_max)]

def distance(point_a, point_b):
    return sqrt((point_a[0]-point_b[0])**2 + (point_a[1]-point_b[1])**2)

origo = [0, 0]
points_inside = 0
points_total = 0
number_of_itterations = 1000000

for i in range(number_of_itterations):
    if distance(random_point2D(), origo) <= 1:
        points_inside += 1
    points_total += 1

print(4*points_inside/points_total)
