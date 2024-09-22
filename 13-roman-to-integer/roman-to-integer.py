class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0

        for index in range(len(s)):
            if index + 1 < len(s) and romans[s[index]] < romans[s[index + 1]]:
                result -= romans[s[index]]
            else:
                result += romans[s[index]]
        
        return result

