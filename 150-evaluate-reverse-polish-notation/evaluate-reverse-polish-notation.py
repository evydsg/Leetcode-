class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token in operators and len(stack) >= 2:
                operand2 = stack.pop()
                operand1 = stack.pop()

                if token == operators[-1]:
                    result = int(operand1 / operand2)
                else:
                    expression = f"{operand1}{token}{operand2}"
                    result = eval(expression)
                
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack[-1]
        