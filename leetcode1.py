nums=[2,7,11,5]
target=9

def twoSum(nums:list[int],target:int)->list[int]:
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
            
list1=twoSum(nums,target)
print(list1)