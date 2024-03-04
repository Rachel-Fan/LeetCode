
def removeDuplicates(nums):
    leng = len(nums)
    output = []
    output.append(nums[0])
    for i in range(1,leng):
        if nums[i] != nums[i-1]:
            output.append(nums[i])
    k = len(output)
    nums = output
    print(k)
    print(nums)

nums = [1,1,2]
removeDuplicates(nums)
