def twosum(nums,target):
    output=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                output.append(i)
                output.append(j)
    return output



num=[2,7,11,15]
target=9
output=twosum(num,target)
print(output)