class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}

        for index, number in enumerate(nums):
            difference = target - number

            if difference in dictionary:
                return [dictionary[difference], index]
            
            dictionary[number] = index
        