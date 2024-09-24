class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        index, length = 0, min(len(ransomNote), len(magazine))
        dictionaryM = {}
       
        for character in magazine:
            if character in dictionaryM:
                dictionaryM[character] += 1
            else:
                dictionaryM[character] = 1
        
        for character in ransomNote:
            if character in dictionaryM:
                dictionaryM[character] -= 1

                if dictionaryM[character] == 0:
                    del dictionaryM[character]
            
            else:
                return False
        
        return True
        