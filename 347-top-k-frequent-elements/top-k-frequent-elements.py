class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freqDict = {}

        for num in nums:
            if num in freqDict:
                freqDict[num] += 1
            else:
                freqDict[num] = 1
        
        freqDict = dict(sorted(freqDict.items(), key = lambda item:item[1], reverse = True))
        
        for key in freqDict:
            result.append(key)
        
        return result[:k]
        