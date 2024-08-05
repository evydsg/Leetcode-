class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
            Understand
                - The idea is to check if any of the values appear twice in the array

                Questions
                    - Are we always guaranteed to find duplicates in the list?
                    - Can we have an empty list?
                
            Match
                - Use dictionaries to keep track of how many times it appears
            
            Plan
                - Check if list is empty
                    - Yes, return list
                - Initialize a dictionary
                - Traverse through the list
                    - If the element is not in the list
                        - We add
                    - Else
                        Change the value to true
            
            Evaluate
                - Time complexity: O(N)
                - Space complexity: O(N)
        """
        
        if nums is None:
            return nums

        dictionary = {}

        for num in nums:
            if num in dictionary:
                dictionary[num] = True
                return True
            else:
                dictionary[num] = False
        
        return False