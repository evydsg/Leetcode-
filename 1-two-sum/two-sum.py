class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevHash = {}

        for index, number in enumerate(nums):
            diff = target - number

            if diff in prevHash:
                return [prevHash[diff], index]
            
            prevHash[number] = index
        