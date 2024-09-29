class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = {}

        for index, character in enumerate(s):
            if character in frequency:
                frequency[character][1] += 1
            else:
                frequency[character] = [index, 1]
        
        for key in frequency:
            if frequency[key][1] == 1:
                return frequency[key][0]
        
        return -1