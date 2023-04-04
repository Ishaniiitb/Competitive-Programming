def sum(lst, target):
    nums = {}
    for i in range(len(lst)):
        d = lst[i]
        required = target - d
        if required in nums:
            return [nums[required], i]
        else:
            nums[d] = i
    return []
