class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)

        if length > 1:
            middle = length // 2

            left_nums = nums[:middle]
            right_nums = nums[middle:]

            self.sortArray(left_nums)
            self.sortArray(right_nums)

            self.merge(nums, left_nums, right_nums)

        return nums
    
    def merge(self, nums, left_nums, right_nums):
        length_left = len(left_nums)
        length_right = len(right_nums)

        left_ptr = 0
        right_ptr = 0
        main_ptr = 0

        while left_ptr < length_left and right_ptr < length_right:

            if left_nums[left_ptr] <= right_nums[right_ptr]:
                nums[main_ptr] = left_nums[left_ptr]
                left_ptr +=1

            else:
                nums[main_ptr] = right_nums[right_ptr]
                right_ptr +=1 
            
            main_ptr +=1

        while left_ptr < length_left:
            nums[main_ptr] = left_nums[left_ptr]
            left_ptr +=1
            main_ptr +=1
        
        while right_ptr < length_right:
            nums[main_ptr] = right_nums[right_ptr]
            right_ptr +=1
            main_ptr +=1
        