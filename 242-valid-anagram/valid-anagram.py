class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
            Understand
                - The idea is to check whether the strings are the same if they are sorted

                Questions
                    - Can we have empty strings?
                    - Are we always guaranteed to have a string that has lowercase letters?
                    - Can a string have any other character than lowercase letters?

            Match
                - Dictionaries, to keep track of the letters and how many times they show up in the string

            Plan
                - Check if any of the string is empty?
                    - return false
                - Check if both strings are empty
                    - return true
                - Initialize two dictionaries
                    - for s string
                    - for t string
                - Traverse through the strings
                    - Increment count if the character is there
                - Compare both dictionaries
                    - Equal return true
            
            Evaluate
                - Time Complexity: O(N), since we traverse through the dictionary
                - Space Complexity: O(N), memory for the dictionaries

        """
        if len(s) == 0 and len(t):
            return True

        if len(s) == 0:
            return False
        
        if len(t) == 0:
            return False

        dict_s = {}
        dict_t = {}

        for character in s:
            if character in dict_s:
                dict_s[character] += 1
            else:
                dict_s[character] = 1
        
        for character in t:
            if character in dict_t:
                dict_t[character] += 1
            else:
                dict_t[character] = 1
        
        if dict_s == dict_t:
            return True
        
        return False
