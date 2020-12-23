
from collections import defaultdict


if __name__ == "__main__":
    start = "9,12,1,4,17,0,18".split(",")
    
    #seq = {int(i):[ix] for ix, i in enumerate(start)}
    seq = defaultdict(list)
    for ix, i in enumerate(start):
        seq[int(i)].append(ix+1)
    last = 18

    #N = 2020
    N = 30000000
    for i in range(8,N+1):
        if len(seq[last]) > 1:
            n = seq[last][-1] - seq[last][-2]
            seq[n].append(i)
            last = n
        else:
            seq[0].append(i)
            last=0
    print(f"Ans 2: {last}")