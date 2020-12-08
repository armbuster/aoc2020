
from itertools import chain
import numpy as np





def parse(s):
    A,B = tuple(s.split(" contain "))
    if B == "no other bags.":
        return
    A = A[:-4].split(" bag")[0].strip()
    B = [b.split(" bag")[0].strip() for b in B.split(", ")]
    num_subbags = [int(b[0]) for b in B]
    color_subbags = [b[2:] for b in B]
    subbags = list(zip(num_subbags, color_subbags))
    return (A, subbags)






def bfs(start, A, color_lookup):
    frontier = [start]
    colors = []
    while frontier:
        v = frontier.pop()
        frontier+=list(np.where(A[v,:] > 0)[0])
        colors.append(color_lookup[v])
    return colors



def dfs(v, A, count):
    next_level = list(np.where(A[v,:] > 0)[0])
    current = 0
    if len(next_level) == 0:
        return count

    for n in next_level:
        current+=dfs(n, A, A[v,n])
    return current * count + count






if __name__ == "__main__":

    constraints = open("../inputs/day7.txt", "r").readlines()
    bags = []
    for s in constraints:
        bag = parse(s.strip())
        if bag is not None:
            bags.append(bag)

    allcolors = set([bag[0] for bag in bags] + list(chain(*[[color for (n,color) in subbag] for _, subbag in bags])))
    color_ind = {c:i for i,c in enumerate(allcolors)}
    color_ind_reverse = {i:c for c,i in color_ind.items()}

    adj = np.zeros((len(color_ind), len(color_ind)), dtype=np.int32)

    # bag constraints are represented as a DAG
    # construct adjacency matrix
    for outer_bag, inner_bags in bags:
        for n, inner_bag in inner_bags:
            adj[color_ind[outer_bag], color_ind[inner_bag]]+=n
    
    adj_t = adj.T
    parents = bfs(color_ind['shiny gold'], adj_t, color_ind_reverse)
    print(f"Ans #1: {len(set(parents))-1}")
    
    ans2 = dfs(color_ind['shiny gold'], adj, 1)
    print(f"Ans #2: {ans2 -1}")


    

