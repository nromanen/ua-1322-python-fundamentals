#https://www.codewars.com/kata/simple-find-the-distance-between-two-points

import math

def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(dist, 2)


print(distance(1, 2, 4, 6))
