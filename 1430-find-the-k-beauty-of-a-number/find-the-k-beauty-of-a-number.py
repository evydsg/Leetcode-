class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        left = 0
        count = 0
        number = ""
        numString = str(num) #

        for index in range(len(numString)):
            
            number += numString[index] #240

            while len(number) > k:
                number = number[1:]
        
            if len(number) == k and int(number) != 0 and num % int(number) == 0:
                count += 1

        return count