class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index, jindex = 0, 0

        while index < len(s) and jindex < len(t):
            if s[index] == t[jindex]:
                index += 1
            
            jindex += 1

        return index == len(s)