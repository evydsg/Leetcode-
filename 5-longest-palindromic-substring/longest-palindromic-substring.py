"""
    Understand: The idea is to return the longest palindrome that can be found in the string
        - Can the string be empty?
        - Are we always guaranteed to have a palindrome?

    Match
        Two Pointers
    
    Plan
        Initialize a variable to keep track of the result
        Traverse through the string
        Initialize the two pointers
            While character at left is equal to right
                Continue adding
                Move pointers
            Keep the longest substring
        Return substring

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        substring = ""
        
        for index in range(len(s)):
            left, right = index, index

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(substring):
                    substring = s[left:right + 1]
                
                left -= 1
                right += 1
            
            left, right = index, index + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(substring):
                    substring = s[left: right + 1]
                
                left -= 1
                right += 1
        
        return substring