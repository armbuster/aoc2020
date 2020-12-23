







def apply_mask(mask, k):
    n=0
    m=2**35
    for i in range(36):
        if mask[i]=='X':
            n |= m & k
        elif mask[i]=="1":
            n |= m
        m>>=1
    return n


from itertools import combinations



def apply_mask2(mask, k):
    nums = []
    m=2**35
    for i in range(36):
        if mask[i]=='X':
            nums.append(m)
            k &= ~m
        elif mask[i]=='1':
            k |= m
        m>>=1
    results = [k]
    for i in range(1, len(nums)+1):
        combos = combinations(nums, i)
        for combo in combos:
            results.append(k+sum(combo))
    
    return results

            




if __name__ == "__main__":
    instructions = open("../inputs/day14.txt", "r").read().splitlines()
    instructions = [tuple(k.split(" = ")) for k in instructions]
    mem = {}

    for op, val in instructions:
        if op == "mask":
            mask = val
        else:
            n = apply_mask(mask, int(val))
            exec(op+"="+str(n))
    print(f"Ans 1: {sum([v for (k,v) in mem.items()])}")



    mem = {}
    for op, val in instructions:
        if op == "mask":
            mask = val
        else:
            nums = apply_mask2(mask, int(op[4:-1]))
            for n in nums:
                mem[n]=int(val)
    print(f"Ans 2: {sum([v for (k,v) in mem.items()])}")