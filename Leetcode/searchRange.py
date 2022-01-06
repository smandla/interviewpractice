def binarySearch(nums, target, leftbias):
    low = 0 
    high = len(nums) - 1
    i = -1
    print(i)
    while low <= high: 
        mid = (low + high) // 2
        print(mid)
        if (nums[mid] == target):
            i = mid
            if leftbias:
                high = mid - 1
            else:
                low = mid + 1
        elif nums[mid] > target: 
            high = mid - 1
        else:
            low = mid + 1
    return i 

def searchRange(nums, target):
    left = binarySearch(nums, target, True)
    right = binarySearch(nums, target, False)
    return [left, right]


nums = [5, 7, 7, 8, 7, 10]
target = 7 
print(searchRange(nums, target))