class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
            Understand
                The idea is to perform the arithmetic expression

                Are we always guaranteed to only receive operators and operands?
                Can we get negative integers?
                Can we receive an empty string?

            Match
                Stack

            Plan
                Check if list is empty
                Initialize a stack
                Traverse through the list
                    If it is an operator
                        Remove the last two elements
                        Perform the calculation
                        Append it to the stack
                    Else
                        Convert to integers
                        Insert into the stack
                    
        """
        if len(tokens) == 0:
            return 0
        
        stack = []

        for string in tokens:
            if string == '+':
                if len(stack) >= 2:
                    operand1 = stack.pop()
                    operand2 = stack.pop()
                    calculation = operand1 + operand2
                    stack.append(calculation)
            elif string == '-':
                if len(stack) >= 2:
                    operand1 = stack.pop()
                    operand2 = stack.pop()
                    calculation = operand2 - operand1
                    stack.append(calculation)
            elif string == '*':
                    if len(stack) >= 2:
                        operand1 = stack.pop()
                        operand2 = stack.pop()
                        calculation = operand2 * operand1
                        stack.append(calculation)
            elif string == "/":
                if len(stack) >= 2:
                    operand1 = stack.pop()
                    operand2 = stack.pop()

                    if operand1 != 0:
                        calculation = int(operand2/operand1)
                        stack.append(calculation)
            else:
                stack.append(int(string))
            
        return stack[-1]
