class Solution:
    def fib(self, n: int) -> int:
        """
            Understand
                The idea is to to calculate the fibonacci sequence of a number

                Questions
                    Can we get a number that is negative?
            
            Match
                Recursion

            Plan
                Verify if number is 0
                    Yes, return 0
                Verify if number is 1
                    Yes return 1
                If number > 1
                    return fib(n-1) + f(n-2)

        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        return self.fib(n - 1) + self.fib(n-2)