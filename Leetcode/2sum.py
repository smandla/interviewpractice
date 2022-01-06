def twosum(nums, target):
    ht = {}
    n = len(nums) - 1
    for i in range(0, n):
        complement = target - nums[i]
        if complement in ht:
            return ht[complement], i
        ht[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9
print(twosum(nums, target))