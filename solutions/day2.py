
from collections import Counter




def isPasswordValidPartOne(constraint, letter, counts):
    a,b = constraint
    if letter in counts and counts[letter] >= a and counts[letter] <= b:
        return True
    return False

def isPasswordValidPartTwo(constraint, letter, passwd):
    a,b = constraint
    a-=1
    b-=1
    x,y = (passwd[a], passwd[b])
    if x!=letter and y!=letter:
        return False
    if x==letter and y==letter:
        return False
    return True





if __name__ == "__main__":
    lines = open("inputs/day2.txt", "r").read().split("\n")
    passwords = [tuple(l.split(" ")) for l in lines]
    constraints = list(map(lambda x: tuple([ int(i) for i in x[0].split("-")]), passwords))
    letters = list(map(lambda x: x[1][0], passwords))
    counters = list(map(lambda x: Counter(x[2]), passwords))
    args = list(zip(constraints, letters, counters))
    
    isValid = map(lambda x: isPasswordValidPartOne(*x), args)
    print(f"Answer 1: {sum(isValid)}")

    args = list(zip(constraints, letters, [x[2] for x in passwords]))
    isValid = map(lambda x: isPasswordValidPartTwo(*x), args)
    print(f"Answer 2: {sum(isValid)}")
