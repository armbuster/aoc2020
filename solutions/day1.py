






if __name__ == "__main__":
    with open("../inputs/day1.txt", "r") as f:
        nums = [int(i) for i in f.read().split("\n")]
    set_nums = {i:2020-i for i in nums}
    
    for i in set_nums:
        if set_nums[i] in set_nums:
            print(f"Answer 1: {set_nums[i] * i}")
            break
    done=False
    for ix, i in enumerate(nums):
        for j in range(ix+1, len(nums)):
            if 2020 - i - nums[j] in set_nums:
                ans2 = (2020 - i - nums[j]) * i * nums[j]
                print(f"Answer 2: {ans2}")
                done=True
                if done:
                    break
            if done:
                break


    