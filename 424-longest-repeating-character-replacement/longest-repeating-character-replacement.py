class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count, result, left = {}, 0, 0

        for index in range(len(s)):
            count[s[index]] = 1 + count.get(s[index], 0)

            while index - left + 1 - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            
            result = max(result, index - left + 1)
        
        return result