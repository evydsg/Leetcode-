class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        divider = 1

        while x >= divider * 10:
            divider *= 10
        
        while x != 0:
            right = x % 10
            left = x // divider

            if left != right:
                return False
            
            x = (x % divider) // 10
            divider = divider // 100
        
        return True