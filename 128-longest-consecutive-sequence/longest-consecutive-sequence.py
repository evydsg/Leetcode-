class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        result = 0

        for number in nums:
            if number - 1 not in nums:
                temporary = number
                count = 1

                while temporary + 1 in nums:
                    temporary = temporary + 1
                    count += 1
                
                result = max(count, result)
        
        return result