class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        index, result = 0, 0

        while index < len(target):
            prev_index = index

            for character in source:
                if index < len(target) and character == target[index]:
                    index += 1
                
            if index == prev_index:
                return -1
        
            result += 1
        
        return result