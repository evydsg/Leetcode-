class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 0:
            return ""

        result = "1"

        while n > 1:
            current = ""
            index = 0

            while index < len(result):
                count = 1
                
                while index + 1 < len(result) and result[index] == result[index + 1]:
                    count += 1
                    index += 1
                current += str(count) + result[index]
                index += 1

            result = current

            n -= 1
        
        return result