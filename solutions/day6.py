

def countletters(s):
    return len(set(s.replace("\n","")))

def countintersect(s):
    sets = [set(i) for i in s.split("\n")]
    return len(sets[0].intersection(*sets[1:]))





if __name__ == "__main__":
    forms = open("../inputs/day6.txt", "r").read().split('\n\n')
    part1 = sum(map(countletters, forms))
    print(f"Ans 1: {part1}")
    part2 = sum(map(countintersect, forms))
    print(f"Ans 2: {part2}")