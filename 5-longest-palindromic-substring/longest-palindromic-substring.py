class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        for index in range(len(s)):
            left, right = index, index

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(result):
                    result = s[left: right + 1]
                
                left -= 1
                right += 1
            
            left, right = index, index + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(result):
                    result = s[left: right + 1]
                
                left -= 1
                right += 1
            
        return result