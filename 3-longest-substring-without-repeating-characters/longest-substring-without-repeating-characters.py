class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        longestS = 0

        for index in range(len(s)):
            while s[index] in substring:
                substring = substring[1:]
            
            substring += s[index]
            longestS = max(len(substring), longestS)
        
        return longestS
