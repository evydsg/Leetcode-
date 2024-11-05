class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if len(nums)== 0:
            return []
        
        ans = nums + nums
        return ans
        