class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0

        for index in range(len(nums)):
            if leftSum == total - leftSum - nums[index]:
                return index

            leftSum += nums[index]

        return -1        