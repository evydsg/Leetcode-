class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        result = 0

        for num in nums:
            if num - 1 not in nums:
                current = num
                count = 1

                while current + 1 in nums:
                    current = current + 1
                    count += 1
                
                result = max(count, result)
        
        return result