def threeConsecutiveOdds(arr):
    for i in range(0, len(arr) - 2):
        print('The i item is', arr[i])
        
        # Check if the current element and the next two elements are odd
        if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
            return True
    return False
            
arr = [1,2,34,3,4,5,7,23,12]
threeConsecutiveOdds(arr)
    