
def majorityElement(nums):
    hash = {}
    res = majority = 0

    for n in nums:
        hash[n] = hash.get(n,0) +1
        print(hash)
        if hash[n] > majority:
            res = n
            majority = hash[n]

    return res


nums = [2,2,1,1,1,2,4,3,3,2]
res = majorityElement(nums)

print(res)