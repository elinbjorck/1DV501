from random import uniform
from math import sqrt
from math import pi

x_min, x_max = -1, 1
y_min, y_max = -1, 1
origo = [0, 0]

def random_point2D():
    return [uniform(x_min, x_max), uniform(y_min,y_max)]

def distance(point_a, point_b):
    return sqrt((point_a[0]-point_b[0])**2 + (point_a[1]-point_b[1])**2)

def monte_carlo_circle(number_of_itterations):
    points_inside = 0
    for _ in range(number_of_itterations):
        if distance(random_point2D(), origo) <= 1:
            points_inside += 1
    return 4*points_inside/number_of_itterations

pi_100 = monte_carlo_circle(100)
pi_10000 = monte_carlo_circle(10000)
pi_1000000 = monte_carlo_circle(1000000)

error_100 = abs(pi_100-pi)
error_10000 = abs(pi_10000-pi)
error_1000000 = abs(pi_1000000-pi)

print(f'With 100 random points the value of pi is approximated to: {pi_100} and the error is {error_100}.')
print(f'With 10000 random points the value of pi is approximated to: {pi_10000} and the error is {error_10000}.')
print(f'With 1000000 random points the value of pi is approximated to: {pi_1000000} and the error is {error_1000000}.')
