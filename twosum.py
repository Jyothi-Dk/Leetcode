
nums=[2,3,5,6,4,7,0,11]
target=8


num_map={}
def two_sum(nums,target):
    l=len(nums)
    for i in range(l):
        diff=target-nums[i]
        if diff in num_map:
           print([num_map[diff],i])
        num_map[nums[i]]=i
    
    

    

two_sum(nums,target)
