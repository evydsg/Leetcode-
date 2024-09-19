class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevDic = {}

        for index, number in enumerate(nums):
            if (target - number) in prevDic:
                return [prevDic[(target - number)], index]
            
            prevDic[number] = index