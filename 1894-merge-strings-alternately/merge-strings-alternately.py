class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        l1, l2 = 0, 0

        while l1 < len(word1) and l2 < len(word2):
            merged += word1[l1]
            merged += word2[l2]

            l1+= 1
            l2+= 1

        while l1 < len(word1):
            merged += word1[l1]
            l1 += 1

        while l2 < len(word2):
            merged += word2[l2]
            l2 += 1
        
        return merged
        