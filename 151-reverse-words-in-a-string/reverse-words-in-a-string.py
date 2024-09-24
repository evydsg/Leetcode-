class Solution:
    def reverseWords(self, s: str) -> str:
        List = s.split()
        left, right = 0, len(List) - 1
        
        while left < right:
            List[left], List[right] = List[right], List[left]
            left += 1
            right -= 1
	    
        return " ".join(List)