class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring, lenSub, index = "", 0, 0

        while index in range(len(s)):
            while s[index] in substring:
                substring = substring[1:]
            
            substring += s[index]
            lenSub = max(lenSub, len(substring))
            index += 1
        
        return lenSub
        