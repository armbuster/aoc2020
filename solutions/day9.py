


# return true if there are two numbers in s that sum to t
def twosum(s, t):
    for i in range(len(s)):
        if (t - s[i]) in s and (t-s[i]) != s[i]:
            return True
    return False







if __name__ == "__main__":
    nums = open("../inputs/day9.txt", "r").readlines()
    nums = [int(n.strip()) for n in nums]
    
    nums = []
    last25 = set()
    for i in range(25):
        n = nums[i]
        nums.append(n)
        #last25.add(n)

    for i in range(26, len(forms)):
        
        n = nums[i]
        
        if not twosum(nums, n):
            print(f"Ans 1: {n}")
        nums = nums[1:]
        nums.append(n)

    # Part 2
    T = 22406676
    i,k = 0,1
    while True:
        if sum(nums[i:k]) < T:
            k+=1
        elif sum(nums[i:k]) > T:
            i+=1
        else:
            print(f"Ans 2: {min(nums[i:k]) + max(nums[i:k])}")
            break


