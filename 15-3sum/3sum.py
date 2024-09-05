class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = [] #Return the list of results

        nums.sort()
        # nums = [-4, -1, -1, 0, 1, 2]

        for index in range(len(nums)):

            if index > 0 and nums[index] == nums[index-1]:
                continue
                
            left, right = index + 1, len(nums)-1
        
            
            while left < right:
                sum_nums = nums[index] + nums[left] + nums[right]

                if sum_nums < 0:
                    left += 1
                elif sum_nums > 0:
                    right -= 1
                else:
                    result.append([nums[index], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1

        return result