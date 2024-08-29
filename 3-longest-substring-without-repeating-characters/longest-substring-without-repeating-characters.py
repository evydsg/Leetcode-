class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            Understand
                Find the length of the longest substring without repeating characters

                Can we have duplicates?
                Are we always guaranteed to have letters in s or can we have other characters?
                What should we return if there are only duplicates?

                01234567
                abcabcbb
                
                L
                  R

            Match
                Slinding Window

            Plan
                Check if the length of the string is 0 or if string is empty
                Initialize a variable to keep track of the longest substring
                Initialize one pointer to start from the beginning
                Iterate through the string
                    If character [r] not in string
                        Increment R
                        Append character[r] to the string
                    Else:
                        increment both left

        """
        if len(s) == 0:
            return 0
        
        left = 0
        substring = ""
        max_length = 0

        for right in range(len(s)):
            if s[right] not in substring:
                substring += s[right]
                max_length = max(max_length, len(substring))
            else:
                while s[right] in substring:
                    substring = substring[left+1:]
                substring += s[right]
        
        return max_length



        