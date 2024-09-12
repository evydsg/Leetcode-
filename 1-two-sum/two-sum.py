class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}

        for index in range(len(nums)):
            difference = target - nums[index]

            if difference in dictionary:
                return [dictionary[difference], index]
            
            dictionary[nums[index]] = index
        
        