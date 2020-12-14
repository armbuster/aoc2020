




from collections import Counter









if __name__ == "__main__":
    nums = open("inputs/day10.txt", "r").readlines()
    nums = [int(n.strip()) for n in nums]
    nums = sorted(nums)
    nums = [0] + nums + [nums[-1] + 3]
    diff = [nums[i]-nums[i-1] for i in range(1,len(nums))]
    counts = Counter(diff)
    print(f"Ans 1: {counts[1] * counts[3]}")


    # options[i] - for a chain ending with nums[i], how many options are there
    # for the next jolt
    options = [1]
    for i in range(len(nums)-1):
        options.append(sum([nums[i]+k in nums for k in (1,2,3)]))

    # counts[i] - how many chains ending with nums[i] are there currently    
    counts = [0] * len(nums)
    counts[0] = 1

    # add # of chains ending with nums[i] for each additional jolt that could be added
    for i in range(len(nums)-1):
        for j in range(i+1, i+1+options[i]):
            counts[j]+=counts[i]

    print(f"Ans 2: {counts[-1]}")

    

    # dp[i] - how different devices could go after device i
    # T[i] - how many different ways could the first i-1 devices be arranged
    

    







    



