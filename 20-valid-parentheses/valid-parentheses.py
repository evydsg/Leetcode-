class Solution:
    def isValid(self, s: str) -> bool:
        """
            Understand
                - The idea is to check if the open brackets are closed by the same type of brackets and in the same order

                Questions
                    - Can we have an empty string?
                    - Are we always guaranteed to have just characters that are brackets?

            Match
                - Stack
            
            Plan
                - Check if string is empty
                    Yes, return true
                - Initialize a stack
                - Traverse through the string
                    - If bracket is a closing bracket
                        - Check if top element of the stack corresponds to the bracket
                        - If not, return false
                    - Else
                        - Insert into the stack
                - If stack is empty
                    - Return true
                - Return False
        """

        if len(s) == 0:
            return True

        stack = []

        for bracket in s:
            if bracket == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif bracket == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif bracket == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        return len(stack) == 0


