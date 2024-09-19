class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largestSum, currentSum = nums[0], 0
        
        for num in nums:
            if currentSum < 0:
                currentSum = 0
            
            currentSum += num
            largestSum = max(currentSum, largestSum)
        
        return largestSum