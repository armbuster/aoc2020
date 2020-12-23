import numpy as np



cayley = """1 2 3 4 5 6 7 8
2 3 4 1 8 7 5 6
3 4 1 2 6 5 8 7
4 1 2 3 7 8 6 5
5 7 6 8 1 3 2 4
6 8 5 7 3 1 4 2
7 6 8 5 4 2 1 3
8 5 7 6 2 4 3 1""".split("\n")
cayley = [c.split(" ") for c in cayley]
cayley = [[int(i)-1 for i in row] for row in cayley]



import pdb


R0 = lambda x: x
R90 = lambda x: np.rot90(x)
R180 = lambda x: np.rot90(x, k=2)
R270 = lambda x: np.rot90(x, k=3)
H = lambda x: np.flipud(x)
V = lambda x: np.fliplr(x)
D = lambda x: np.rot90(np.fliplr(x))
D_ = lambda x: np.rot90(np.flipud(x))

D4 = [R0, R90, R180, R270, H, V, D, D_]

S = ['R0', 'R90', 'R180', 'R270', 'H', 'V', 'D', 'D_']
S = dict(zip(S, range(8)))
#D4_inv = dict(zip(range(8), [np.where([i==0 for i in cayley[k]])[0][0] for k in range(8)])))






def count_matching_edges(i):
    assert i in squares

    other_squares = set(squares.keys())
    other_squares.remove(i)

    matches = 0
    for k in other_squares:
        for f_k in D4:
            for f_i in D4:
                matches+=np.array_equal(f_k(squares[k])[0,:], f_i(squares[i])[0,:])
    return matches
    

        

# def find_matching_squares(i):
#     assert i in squares

#     other_squares = set(squares.keys())
#     other_squares.remove(i)

#     matches = []
#     for k in other_squares:
#         for edge in squares[i]:
#             for ix, edge_ in enumerate(squares[k]):
#                 if np.array_equal(edge, edge_):
#                     matches.append((k, ix))
#     return matches
    

def find_match(squares, i, S, slice_funcs):
    sq = set(squares.keys())
    sq.remove(i)

    f = slice_funcs[S]
    w = slice_funcs[(S+2)%4]

    t = f(squares[i])

    for k in sq:
        d4_squares = [g(squares[k]) for g in D4]
        for ix, m in enumerate(d4_squares):
            if np.array_equal(t, w(m)):
                return k, ix








if __name__ == "__main__":
    f = open("../inputs/day20.txt", "r").read()
    tiles = f.split("\n\n")
    squares = {}
    original_squares = {}

    for tile in tiles:
        id, sq = tile.strip().split(":\n")
        _, id = id.split(" ")
        id = int(id)
        sq = sq.replace("#","1")
        sq = sq.replace(".","0")
        sq = sq.split("\n")
        sq = np.array([[int(i) for i in row] for row in sq])
        #original_squares[id] = sq
        squares[id] = sq

    square_ids = list(squares.keys())
    match_counts = list(map(count_matching_edges, square_ids))
    print(f"Ans {1}: {np.prod([square_ids[ix] for ix, i in enumerate(match_counts) if i==4])}")


    #########################
    ####  Squares ###########
    #########################



    # get starting square to fix position, must have 4 neighbors
    stack = []
    for ix,k in enumerate(match_counts):
        if k==8:
            start = square_ids[ix]
            break
    
    #K_=7
    #original_squares[start] = D4[K_](original_squares[start]) # shift this square to new orientation
    #squares[start] = [f(original_squares[start])[0,:] for f in D4]

    symmetries = {start:0}
    stack.append(start)
    neighbors = {id:[None] * 4 for id in squares.keys()}
    slice_funcs = [lambda x: x[0,:], lambda x: x[:,-1], lambda x: x[-1,:], lambda x: x[:,0]]
    # top, right, bottom, left

    processed = set()

    #squares that have already been assigned cannot change orientation
    while stack:
        current = stack.pop()
        for S in range(4): # make sure this shouldnt be S_inv
            if neighbors[current][S] is None:
                match = find_match(squares, current, S, slice_funcs)
                
                # once squares are matched they cannot be shifted again
                if match is not None:
                    sq_id, K = match
                    #S_inv = (4-S)%4
                    #K_ = cayley[cayley[S_inv][2]][K] # S_inv * R180 * V

                    #if neighbors[sq_id][(S+2)%4] is None:
                    # if sq_id in processed:
                    #     assert K_==0
                    #     pdb.set_trace()
                    # if sq_id == 2311:
                    #     pdb.set_trace()
                    if K != 0:
                        assert all([i is None for i in neighbors[sq_id]])
                    
                        
                    symmetries[sq_id] = K
                    #original_squares[sq_id] = D4[K_](original_squares[sq_id]) # shift this square to new orientation
                    squares[sq_id] = D4[K](squares[sq_id])
                    
                    neighbors[current][S]=sq_id # set this square as neighbor of current

                    assert neighbors[sq_id][(S+2)%4] is None or neighbors[sq_id][(S+2)%4]==current
                    #assert np.array_equal(squares[current][S], squares[sq_id][(S+2)%4])

                    neighbors[sq_id][(S+2)%4]=current
                    if sq_id not in processed:
                        stack.append(sq_id) # find neighbors of this square
                    processed.add(sq_id) # this square cant match another square
    
    
    
    print(np.prod([k for k in neighbors.keys() if sum([i is None for i in neighbors[k]])==2]))
    sea = np.zeros((96,96))

    # find top left square
    for current in neighbors:
        N = neighbors[current]
        if N[0] is None and N[3] is None:
            break
    
    # 2473
    count=0
    i=0
    j=0
    next_row, next_col = 0,0
    while current is not None:
        next_row = neighbors[current][2]
        while current is not None:
            next_col = neighbors[current][1]
            sea[i:i+8, j:j+8] = squares[current][1:-1,1:-1]
            j+=8
            current=next_col
        current=next_row
        j=0
        i+=8
    
    #import matplotlib.pyplot as plt
    #plt.imshow(sea)
    #plt.show()

    sea = sea.astype(bool)

    def s_to_array(s):
        s=s.replace("#","1").replace(" ","0")
        s = s.split("\n")
        s = np.array([[int(i) for i in row] for row in s])
        return s
    
    def find_seamonster(s, arr):
        r,c = arr.shape
        r_, c_ = s.shape
        count = 0

        K = np.sum(s)

        i,j=0,0
        while i <= r-r_:
            j=0
            while j <= c-c_:
                if np.sum(np.logical_and(s, arr[i:i+r_, j:j+c_])) == K:
                    print("seamonster")
                    count+=1
        
                j+=1
            i+=1
        return count
    
    seamonster = s_to_array("""                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """).astype(bool)
    
    for f in D4:
        ans = find_seamonster(seamonster, f(sea))
        if ans != 0:
            break
    print(f"Ans 2: {np.sum(sea) - ans * np.sum(seamonster)}")
                













    



    

            

        


            
