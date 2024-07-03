def moveZeroes(nums):
    n = len(nums)
    if n > 1:
        # Initialize two pointers
        i = 0  # Pointer for iterating through the list
        j = 0  # Pointer for placing non-zero elements

        while i < n:
            if nums[i] > 0:
                nums[j] = nums[i]
                j += 1
            i += 1

        # Fill the rest of the list with zeros
        while j < n:
            nums[j] = 0
            j += 1

    print(nums)
    return nums

nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
