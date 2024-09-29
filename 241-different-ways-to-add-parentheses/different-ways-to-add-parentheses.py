class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operations ={
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y
        }

        def backtrack(left, right):
            result = []
            
            for index in range(left, right + 1):
                operation = expression[index]

                if operation in operations:
                    nums1 = backtrack(left, index - 1)
                    nums2 = backtrack(index + 1, right)

                    for n1 in nums1:
                        for n2 in nums2:
                            result.append(operations[operation](n1, n2))
            if len(result) == 0:
                result.append(int(expression[left : right + 1]))
            return result
        
        return backtrack(0, len(expression) - 1)