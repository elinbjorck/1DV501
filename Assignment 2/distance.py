from math import sqrt

def distance(point_a, point_b):
    """ point a and point b are given as lists of coordinates. They must have the same number of coordinates"""
    if len(point_a) == len(point_b):
        length = len(point_a)
        s = 0
        for i in range(length):
            s += (point_a[i]-point_b[i])**2
        dist = sqrt(s)
        return dist
    else:
        print('Point_a and point_b need to have the same number of coordinates, and they need to be lists.')

point_a = []
point_b = []

point_a.append(int(input('Enter x1: ')))
point_a.append(int(input('Enter x2: ')))
point_b.append(int(input('Enter y1: ')))
point_b.append(int(input('Enter y2: ')))

dist = distance(point_a, point_b)
print(round(dist,3))