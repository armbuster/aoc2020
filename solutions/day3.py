




if __name__ == "__main__":

    trees=0
    position=0
    map = open("inputs/day3.txt", "r")
    for row in map:
        if row[position] == "#":
            trees+=1
        position = (position+3) % (len(row)-1)
    print(f"Part 1: {trees}")


    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    ans=1

    for (x, y) in slopes:
        trees=0
        position=0
        map.seek(0)
        for ix, row in enumerate(map):
            if ix % y == 0:
                if row[position]=="#":
                    trees+=1
                position= (position+x) % (len(row)-1)
        ans*=trees

    print(f"Part 2: {ans}")



