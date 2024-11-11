class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 1:
            return 0

        dictionary = {}
        
        for character in s:
            if character in dictionary:
                dictionary[character] += 1
            else:
                dictionary[character] = 1
        
        for index in range(len(s)):
            if dictionary[s[index]] == 1:
                return index
        
        return -1
