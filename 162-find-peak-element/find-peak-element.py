class Solution:
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:  # Use "<" because we will eventually converge on a peak
            middle = (left + right) // 2

            # Compare middle with its right neighbor
            if nums[middle] < nums[middle + 1]:
                left = middle + 1  # Move to the right
            else:
                right = middle  # Move to the left

        return left


        