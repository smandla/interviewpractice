def arrayOfArrayProducts(nums):
    n = len(nums)
    array = [0] * n
    product = 1
    
    
    for i in range(n):
        array[i] = product
        product *= nums[i]
    
    product = 1
    for i in range(n-1, -1, -1):
        array[i] *= product 
        product *= nums[i]
    print(array)
   
nums = [10, 8, 2]
print(arrayOfArrayProducts(nums))