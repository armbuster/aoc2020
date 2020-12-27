
from collections import defaultdict


def parse_input(s):
    moves = []
    while s:
        if s[0] in ['s','n']:
            moves.append(s[:2])
            s = s[2:]
        else:
            moves.append(s[:1])
            s = s[1:]
    return moves

def add_tuple(a,b):
    return a[0]+b[0], a[1]+b[1], a[2]+b[2]

d = {'ne':(0,1,1), 'e':(1,1,0), 'se':(1,0,-1), 'sw': (0,-1,-1), 'w':(-1,-1,0), 'nw':(-1,0,1)}


if __name__ == "__main__":
    moves = open("../inputs/day24.txt", "r").read().split("\n")
    moves = [parse_input(m) for m in moves]

    black_tiles = set()
    for m in moves:
        pos = (0,0,0)
        for m_ in m:
            #print(m_)
            pos = add_tuple(pos, d[m_])
        
        if pos in black_tiles:
            black_tiles.remove(pos)
        elif pos not in black_tiles:
            black_tiles.add(pos)
    print(f"Ans 1 {len(black_tiles)}")


    for i in range(100):
        adj = defaultdict(int)
        for tile in black_tiles:
            for k in d.keys():
                adj[add_tuple(tile, d[k])]+=1
        
        toadd = set()
        toremove = set()

        white_tiles = set()
        for tile in adj:
            for k in d:
                white_tiles.add(add_tuple(d[k], tile))

        for tile in white_tiles:
            if tile not in black_tiles and adj[tile]==2:
                toadd.add(tile)
        for tile in black_tiles:
            if adj[tile]==0 or adj[tile]>2:
                toremove.add(tile)
        
        for tile in toadd:
            black_tiles.add(tile)
        for tile in toremove:
            black_tiles.remove(tile)
    print(f"Ans 2: {len(black_tiles)}")
        





