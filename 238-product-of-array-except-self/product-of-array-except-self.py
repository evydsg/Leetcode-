class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            Understand
                The idea is to find the product of the array except the current number. 

                Questions
                     Can we have an empty array?
                     
                Edge Cases
                    nums = [1, 1, 1, 1]
                    result = [1, 1, 1, 1]

                    nums = [1, 2, 3, 4]
                    result = [24, 12, 8, 6]
            
            Match 
                Prefix 
            
            Plan
                - Initialize an array for result. It should be the same length as the results list
                    result = [0] * len(nums)
                - Initialize a variable for the first prefix
                    prefix = 1, so that it does not invalidate the product of the array
                - Traverse through the array
                    Calculate the product of each prefix
                        for num in nums:
                            prefix *= num
                            result.append(prefix)

        """
        #Array to append the results
        result = []

        prefix = 1

        #To calculate the product of each number 
        for num in nums:
            result.append(prefix)
            prefix *= num

        postfix = 1

        #To reverse the array from back to start
        for index in range(len(nums)-1, -1, -1):
            result[index] *= postfix
            postfix *= nums[index]
        
        return result

        