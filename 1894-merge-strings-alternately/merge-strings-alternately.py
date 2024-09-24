class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        length = min(len(word1), len(word2))
        index = 0

        while index in range(length):
            merged += word1[index]
            merged += word2[index]
            index += 1
        
        while index < len(word1):
            merged += word1[index]
            index += 1
        
        while index < len(word2):
            merged += word2[index]
            index += 1
        
        return merged
        