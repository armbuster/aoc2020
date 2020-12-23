
from collections import defaultdict

directions = []
for i in range(-1,2):
    for j in range(-1,2):
        for k in range(-1,2):
            directions.append((i,j,k))
directions.remove((0,0,0))


directions = []
for i in range(-1,2):
    for j in range(-1,2):
        for k in range(-1,2):
            for v in range(-1,2):
                directions.append((i,j,k,v))
directions.remove((0,0,0,0))




if __name__ == "__main__":
    f = open("../inputs/day17.txt", "r").read().splitlines()
    cubes = set()
    for i, row in enumerate(f):
        for j, cube in enumerate(row):
            if cube=="#":
                cubes.add((i,j,0))

    for iteration in range(6):
        
        neighbors = defaultdict(int)
        add = []
        remove = []
        for (i,j,k) in cubes:
            for (u,v,w) in directions:
                neighbors[(i+u, j+v, k+w)]+=1
        
        for k, n in neighbors.items():
            if k not in cubes and n==3:
                add.append(k)
        for k in cubes:
            if neighbors[k] not in [2,3]:
                remove.append(k)

        
        for i in add:
            cubes.add(i)
        for i in remove:
            cubes.remove(i)
    print(f"Ans 1: {len(cubes)}")



    ##################
    ## Part 2 ########
    ##################


    f = open("../inputs/day17.txt", "r").read().splitlines()
    cubes = set()
    for i, row in enumerate(f):
        for j, cube in enumerate(row):
            if cube=="#":
                cubes.add((i,j,0,0))

    for iteration in range(6):
        
        neighbors = defaultdict(int)
        add = []
        remove = []
        for (i,j,k,p) in cubes:
            for (u,v,w,y) in directions:
                neighbors[(i+u, j+v, k+w, p+y)]+=1
        
        for k, n in neighbors.items():
            if k not in cubes and n==3:
                add.append(k)
        for k in cubes:
            if neighbors[k] not in [2,3]:
                remove.append(k)

        
        for i in add:
            cubes.add(i)
        for i in remove:
            cubes.remove(i)
    print(f"Ans 2: {len(cubes)}")


