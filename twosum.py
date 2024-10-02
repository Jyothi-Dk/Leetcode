nums=[2,3,5]
target=8

num_map={}

for i in range(len(nums)):
    num_map[nums[i]]=i
    
for i in range(len(nums)):
    diff=target-nums[i]
    if diff in num_map:
        
        flag=True
        
    else:
        flag=False
        
if flag==True:
    print([i,num_map[diff]])
else:
    print(-1)


