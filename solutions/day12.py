from math import pi, sin, cos
import numpy as np
def tuple_add(X, Y):
    return (X[0]+Y[0], X[1]+Y[1])


def tuple_multiply(X, Y):
    return (X[0]*Y[0], X[1]*Y[1])

def rotate(theta, coords):
    y,x=coords
    theta*=(2*pi/360)
    return (int(round(y*cos(theta) + x*sin(theta))), int(round(x*np.cos(theta) - y*sin(theta))))

if __name__ == "__main__":
    nums = open("inputs/day12.txt", "r").readlines()
    moves = [(d[0],int(d[1:].strip())) for d in nums]
    
    # north, east, south, west
    D = [(1,0), (0,1), (-1, 0), (0, -1)]
    i=1 # start east
    location = (0,0)
    d_lookup = {'N':(1,0), "E":(0,1), "S":(-1,0), "W":(0,-1)}

    for U,n in moves:
        if U == "L":
            i = (i-int(n/90)) % 4
        elif U == "R":
            i = (i+int(n/90)) % 4
        elif U == "F":
            location = tuple_add(location, tuple_multiply(D[i], (n,n)))
        else:
            location = tuple_add(location, tuple_multiply(d_lookup[U], (n,n)))
    print(f"Ans 1: {sum((abs(i) for i in location))}")

    W = (1,10)
    location = (0,0)
    for U,n in moves:
        
        if U == "L":
            W = rotate(n, W)
        elif U == "R":
            W = rotate(-n, W)
        elif U == "F":
            location = tuple_add(location, tuple_multiply(W, (n,n)))
        else:
            W = tuple_add(W, tuple_multiply(d_lookup[U], (n,n)))
        print((location, W))
    print(f"Ans 2: {sum((abs(i) for i in location))}")










