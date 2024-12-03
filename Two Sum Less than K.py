class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        result = -1

        while left < right:
            twoSum = nums[left] + nums[right]

            if twoSum < k:
                result = max(twoSum, result)
                left += 1
            else:
                right -= 1
        
        return result