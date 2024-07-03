def intersect(nums1, nums2):
    freq=[0]*10
    print(freq)
    for x in nums1:
        freq[x]+=1
        print('when x is', x, 'freq  is',freq)
    ans=[]
    for x in nums2:
        print('when x is', x)
        if  freq[x]>0:
            ans.append(x)
            print('when x is', x, 'freq  is',freq)
            print('ans is', ans)
            freq[x]-=1
    return ans

nums1 = [0,5,8,7,2,9,7,5]
nums2 = [1,4,8,9]

intersect(nums1, nums2)
