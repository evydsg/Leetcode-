class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sIndex, pIndex = 0, 0
        lastMatch, star = 0, -1

        while sIndex < len(s):
            if pIndex < len(p) and (s[sIndex] == p[pIndex] or p[pIndex] == '?'):
                sIndex += 1
                pIndex += 1
            elif pIndex < len(p) and p[pIndex] == '*':
                lastMatch = sIndex
                star = pIndex
                pIndex += 1
            elif star != -1:
                pIndex = star + 1
                sIndex = lastMatch + 1
                lastMatch = sIndex
            else:
                return False

            
        while pIndex < len(p) and p[pIndex] == "*":
            pIndex += 1
        
        return pIndex == len(p)