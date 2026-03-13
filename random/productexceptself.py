def productExceptSelf(nums):
    n = len(nums)
    res = [1] * n
    
    # 1. Calculate the prefix products (left of index)
    left_product = 1
    for i in range(n):
        res[i] = left_product
        left_product *= nums[i]
        
    # 2. Calculate the suffix products (right of index) and multiply
    right_product = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right_product
        right_product *= nums[i]
        
    return res

print(productExceptSelf([1,2,3,4]))