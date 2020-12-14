

from math import ceil
import numpy as np


# find x such that (A*x)%B==1
def modular_inverse(A, B):
    for x in range(B):
        if A*x % B == 1:
            return x



if __name__ == "__main__":
    nums = open("inputs/day13.txt", "r").readlines()
    K = int(nums[0])
    bus = nums[1].split(",")
    bus = [(ix, int(i)) for ix,i in enumerate(bus) if i != 'x']

    multiples = [ceil(K/i) * i for _,i in bus]
    i = np.argmin(multiples)
    print(f"Ans 1: {bus[i][1] * (multiples[i]-K)}")


    N = np.prod([n for (b,n) in bus])
    BIG_NUMBERS = [int(N/n) for (b,n) in bus]
    inverses = [modular_inverse(BIG_NUMBERS[ix], n)  for ix, (b,n) in enumerate(bus)]

    ans=0
    for i in range(len(bus)):
        ans+=inverses[i]*BIG_NUMBERS[i]*(bus[i][1]-bus[i][0])
    print(f"Ans 2: {ans % N}")
        


    


