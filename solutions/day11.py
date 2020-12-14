
import numpy as np






def search_diagonal(i,j, arr):
    diagonal = np.diagonal(arr, j-i)
    return any(diagonal[j]==2)


if __name__ == "__main__":
    nums = open("inputs/day11.txt", "r").readlines()
    nums =[l.strip().replace('.','0').replace("L",'1') for l in nums]
    nums = np.array([[int(i) for i in l] for l in nums])
    
    # add border of unnoccupied seats on each edge
    nums = np.concatenate((np.array([1] * nums.shape[1]).reshape(1,-1), nums), axis=0)
    nums = np.concatenate((nums, np.array([1] * nums.shape[1]).reshape(1,-1)), axis=0)
    nums = np.concatenate((nums, np.array([1] * nums.shape[0]).reshape(-1,1)), axis=1)
    nums = np.concatenate((np.array([1] * nums.shape[0]).reshape(-1,1), nums), axis=1)
    nums2 = nums.copy()
    bkup = nums.copy()

    done=False
    while not done:
        done=True
        for i in range(1, nums.shape[0]-1):
            for j in range(1, nums.shape[1]-1):
                empty = 0
                full = 0
                if nums[i,j] in [1,2]:
                    for k in range(-1,2):
                        for v in range(-1,2):
                            if not (k==0 and v==0):
                                #print((k,v))
                                empty+=int(nums[i+k,j+v] != 2)
                                full+=int(nums[i+k,j+v] == 2)
                    assert empty+full==8
                    if empty==8 and nums[i,j]==1:
                        done=False
                        nums2[i,j] = 2
                    elif full >=4 and nums[i,j]==2:
                        done=False
                        nums2[i,j] = 1
                    else:
                        nums2[i,j] = nums[i,j]

        nums=nums2.copy()
    
    print(f"Ans 1: {np.sum(nums==2)}")


    directions = [(1,0), (-1,0), (0,1), (0,-1),\
     (1,1), (-1,1), (1,-1), (-1,-1),]

    nums = bkup.copy()
    nums2 = bkup.copy()
    r,c = nums.shape
    done=False
    while not done:
        done=True
        for i in range(1, nums.shape[0]-1):
            for j in range(1, nums.shape[1]-1):
                empty = 0
                full = 0
                if nums[i,j] in [1,2]:
                    for u,v in directions:
                        i_star, j_star =i,j
                        i_star += u
                        j_star += v
                        while nums[i_star,j_star] == 0:
                            i_star+=u
                            j_star+=v
                        full += nums[i_star,j_star]==2
                        empty += nums[i_star,j_star]==1

                    if empty==8 and nums[i,j]==1:
                        done=False
                        nums2[i,j] = 2
                    elif full >=5 and nums[i,j]==2:
                        done=False
                        nums2[i,j] = 1
                    else:
                        nums2[i,j] = nums[i,j]

        nums=nums2.copy()
    
    print(f"Ans 2: {np.sum(nums==2)}")




    



