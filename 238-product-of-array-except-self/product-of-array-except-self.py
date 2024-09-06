class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        prefix, postfix = 1, 1

        for index in range(len(nums)):
            products[index] = prefix
            prefix *= nums[index]
        
        for index in range(len(nums)-1, -1, -1):
            products[index] *= postfix
            postfix *= nums[index]
        
        return products