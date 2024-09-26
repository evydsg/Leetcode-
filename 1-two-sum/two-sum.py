class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevHash = {}

        for index, number in enumerate(nums):
            difference = target - number

            if difference in prevHash:
                return [prevHash[difference], index]
            else:
                prevHash[number] = index