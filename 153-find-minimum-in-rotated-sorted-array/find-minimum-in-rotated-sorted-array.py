class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
            Understand
                Find the minimum element in an array that has been rotated

                Can we have an empty array?
                Can we have an array with only duplicates?

                Original array: 1, 2, 3, 4, 5, 
                0, 1, 2, 3, 4, 5
                3, 4, 5, 6, 1, 2
                L      M        R
                if left >= middle
                

            Plan
                Initialize a variable to keep track of the minimum
                    result = float('inf')
                Initialize two pointers
                    left - start at 0
                    right - start at end
                Iterate through the array using the pointers
                    Keep track of the minimum element
                        min_number = middle
                    Update the result to have the minimum element
                        result = min(min_number, result)
                    Check if the current middle value is greater than or equal left
                        Yes, update the left pointer
                             left = middle + 1
                        No, update the right pointer
                            right = middle - 1
            
            Evaluate
                Time Complexity: O(logn)
                Space Complexity: O(1)
        """
        
        result = nums[0]
        left, right = 0, len(nums)-1

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                return result
            
            middle = (left + right)//2

            result = min(result, nums[middle])

            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1
        
        return result
        