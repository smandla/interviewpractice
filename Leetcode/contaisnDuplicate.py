def containsDuplicate(nums):
    ht = {}
    for i in nums: 
        if i in ht: 
            ht[i] += 1
        else: 
            ht[i] = 1
    for key, val in ht.items():
        if val >= 2: 
            return True
        return False


nums = [1, 2, 3]
print(containsDuplicate(nums))