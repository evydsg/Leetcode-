class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dictionaryS, dictionaryT = {}, {}

        for character in s:
            if character in dictionaryS:
                dictionaryS[character] += 1
            else:
                dictionaryS[character] = 1
        
        for character in t:
            if character in dictionaryT:
                dictionaryT[character] += 1
            else:
                dictionaryT[character] = 1
        
        return dictionaryT == dictionaryS
        