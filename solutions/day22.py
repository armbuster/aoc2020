

import pdb


def recursive_combat(p1, p2, level=0):

    prev_hands = set()

    while p1 and p2:
        if (p1,p2) in prev_hands:
            return 1, p1
            
        else:
            prev_hands.add((p1,p2))
        
        a = p1[0]
        b = p2[0]
        p1 = p1[1:]
        p2 = p2[1:]
        #if type(a) != int:
        #print(a)
        #pdb.set_trace()

        p1_status = a <= len(p1)
        p2_status = b <= len(p2)

        if p1_status and p2_status:
            winner, _ = recursive_combat(p1[:a], p2[:b], level+1)
            #if max(p1[:a]) > max(p2[:b]):
            #    winner = 1
            #elif max(p2[:b]) > max(p1[:a]):
            #    winner = 2
            #else:
            #    assert False
            p1_status = winner == 1
            p2_status = winner == 2
        else:
            p1_status = a>b
            p2_status = b>a

        if p1_status and not p2_status:
            p1 += (a,b)
        elif p2_status and not p1_status:
            p2 += (b,a)
        else:
            assert False
        
    if len(p1)==0:
        return 2, p2
    elif len(p2)==0:
        return 1, p1
    else:
        assert False
    

        









if __name__ == "__main__":
    p1, p2 = open("../inputs/day22.txt", "r").read().split("\n\n")
    p1 = p1.split("\n")
    p2 = p2.split("\n")
    p1 = p1[1:]
    p2 = p2[1:]
    p1 = [int(i) for i in p1]
    p2 = [int(i) for i in p2]

    while p1 and p2:
        a = p1.pop(0)
        b = p2.pop(0)
        if a > b:
            p1.extend([a,b])
        elif b > a:
            p2.extend([b,a])
        else:
            assert False
    if len(p1) > len(p2):
        winner = p1
    else:
        winner = p2
    n=len(winner)
    weights = range(1, n+1)
    winner = list(reversed(winner))
    print(sum([winner[i] * weights[i] for i in range(n)]))




    
    p1, p2 = open("../inputs/day22.txt", "r").read().split("\n\n")
    p1 = p1.split("\n")
    p2 = p2.split("\n")
    p1 = p1[1:]
    p2 = p2[1:]
    p1 = tuple([int(i) for i in p1])
    p2 = tuple([int(i) for i in p2])
    winner, deck = recursive_combat(p1, p2)

    deck = list(reversed(deck))
    n=len(deck)
    weights = range(1, n+1)
    print(sum([deck[i] * weights[i] for i in range(len(deck))]))
