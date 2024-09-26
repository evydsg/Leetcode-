"""
    Understand: the idea is to check if we can find distinct numbers that can add up to 0

        - Can we have an empty array?
        - Is the array sorted?
        - Can we have only duplicates?
    
    Match
        Two Pointers
    
    Plan
        Initialize a variable to return the result
        Sort the array
        Iterate the list
            Initialize two pointers
                left starts after the index
                right starts from the end

                Calculate the sum as long as left pointer and right have not meet
                    if the sum matches 0
                        append to the result
                    else
                        Move pointers


"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for index, number in enumerate(nums):
            if index > 0 and number == nums[index - 1]:
                continue
            
            left, right = index + 1, len(nums)-1

            while left < right:
                threeSum = number + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([number, nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
            
        return result

                    