class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
            Understand
                - The purpose is to return the len of the longest consecutive elements

                Questions
                    - Can we have an array with no consecutive elements?
                    - Can we have an empty array?
            
            Match
                - Set to have only unique numbers
            
            Plan
                - Convert into a set
                - Checkf if lenght of the set is 0
                - Initialize a variable to keep track of the max length 
                - Traverse through the set
                - Check if there is a current_number - 1
                    - Not, set the temporary number to the number
                    - Check if temporaryNumber + 1 is in setNums
                        - Increment length
                        - Make temporaryNumber to be equal to temporaryNumber + 1
                    - Get the max length
            
            Evaluate
                - Time Complexity: O(n), since we traverse through the set
                - Space Complexity: O(n), since we use a set to avoid having duplicates

        """
        set_nums = set(nums)
        length_max = 0

        for num in set_nums:
            if num - 1 not in set_nums:
                temporary_num = num
                length = 1

                while temporary_num + 1 in set_nums:
                    temporary_num = temporary_num + 1
                    length += 1
                
                length_max = max(length_max, length)
            
        return length_max