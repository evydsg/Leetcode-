class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        divider = 1

        while x > divider * 10:
            divider = divider * 10
        
        while x != 0:
            first = x % 10
            last = x // divider

            if first != last:
                return False
            
            x = (x % divider) // 10
            divider = divider / 100
        
        return True
        