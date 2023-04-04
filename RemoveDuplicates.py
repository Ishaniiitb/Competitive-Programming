def removeDuplicates(nums) -> int:
    unique, i = 0, 0
    while i < len(nums):
        num = nums[i]
        nums[unique] = num
        unique += 1
        while i + 1 < len(nums) and nums[i + 1] == num:
            i += 1
        i += 1
    return unique
