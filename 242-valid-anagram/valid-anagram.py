class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dictionary = {}

        for character in s:
            if character in dictionary:
                dictionary[character] += 1
            else:
                dictionary[character] = 1
        
        for character in t:
            if character in dictionary:
                dictionary[character] -= 1

                if dictionary[character] == 0:
                    del dictionary[character]
            
        
        return len(dictionary) == 0