class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        for key in frequency:
            if frequency[key] > len(nums)//2:
                return key
        