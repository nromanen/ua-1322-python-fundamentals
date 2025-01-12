# Program the function distance(p1, p2) which returns the distance between
# the points p1 and p2 in n-dimensional space.
# p1 and p2 will be given as arrays.
# Your program should work for all lengths of arrays, and should return -1
# if the arrays aren't of the same length or if both arrays are empty sets.

def distance(p1, p2):
    from math import sqrt
    if len(p1) == 0 and len(p2) == 0:
        dist = -1
    elif len(p1) != len(p2):
        dist = -1
    else:
        lst_degree = []
        for i in range(len(p1)):
            a = (p2[i] - p1[i]) ** 2
            lst_degree.append(a)
        dist = sqrt(sum(lst_degree))
    return dist
