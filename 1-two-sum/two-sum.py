class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevHash = {}

        for index, num in enumerate(nums):
            difference = target - num

            if difference in prevHash:
                return [prevHash[difference], index]
            else:
                prevHash[num] = index