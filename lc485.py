def findMaxConsecutiveOnes(nums):
    l, output = 0,0
    for r, n in enumerate(nums):
        if n ==0:
            l = r+1
        output = max(output, r-l+1)
    print(output)



nums = [1,0,1,1,0,1]
findMaxConsecutiveOnes(nums)